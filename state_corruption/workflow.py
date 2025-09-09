"""State Corruption & Logic Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="state-corruption")
def factory():
    """Run state corruption & logic vectors detector."""
    return StateCorruptionDetector()


class StateCorruptionDetector(SimpleDetector):
    """Advanced detector covering 25 state corruption & logic attack vectors from VectorGuard Labs."""

    def get_detector_prompt(self) -> str:
        """Define the state corruption & logic vectors detection workflow."""
        return """# State Corruption & Logic Attack Vectors Analysis

## Task
Perform comprehensive analysis of 25 critical state corruption and logic vulnerabilities that exploit low-level EVM mechanisms and storage manipulation.

## Target Attack Vectors

### 🔴 Critical Severity (13 vectors)
1. **Storage Slot Manipulation** - Direct storage manipulation
2. **State Desynchronization** - State inconsistency exploitation
3. **Delegatecall Storage Attack** - Delegatecall storage corruption
4. **Enhanced Delegatecall Attack** - Advanced delegatecall exploitation
5. **Self-Destruct Attack** - Contract destruction exploitation
6. **Enhanced Self-Destruct Attack** - Advanced destruction techniques
7. **CREATE2 Self-Destruct Attack** - CREATE2 + self-destruct combination
8. **Enhanced CREATE2 Self-Destruct** - Advanced destruction attacks
9. **Bytecode Injection Attack** - Runtime bytecode injection
10. **Enhanced Bytecode Injection** - Advanced bytecode attacks
11. **Opcode Manipulation Attack** - Low-level opcode exploitation
12. **Enhanced Opcode Attack** - Advanced opcode manipulation

### 🟡 High Severity (11 vectors)
13. **Variable Corruption** - State variable corruption
14. **Stack Overflow Attack** - Call stack overflow
15. **Function Selector Attack** - Function selector collision
16. **Enhanced Function Selector Attack** - Advanced selector attacks
17. **CREATE2 Deployment Attack** - CREATE2 exploitation
18. **Enhanced CREATE2 Attack** - Advanced CREATE2 attacks
19. **Calldata Manipulation Attack** - Calldata exploitation
20. **Enhanced Calldata Attack** - Advanced calldata attacks
21. **Memory Manipulation Attack** - Memory corruption exploitation
22. **Bytecode Hash Attack** - Bytecode hash manipulation
23. **Enhanced Hash Attack** - Advanced hash attacks

### 🟠 Medium Severity (2 vectors)
24. **Calldata Length Attack** - Calldata length exploitation
25. **Enhanced Length Attack** - Advanced length attacks

## Analysis Process

### 1. Discovery Phase
- Map contract storage layout and proxy patterns
- Identify delegatecall usage and storage context preservation
- Locate CREATE2 factories and deployment mechanisms
- Find assembly blocks and low-level operations
- Analyze upgrade mechanisms and implementation patterns

### 2. Attack Vector Analysis

#### Storage Manipulation Attacks
```solidity
// Direct storage slot access:
assembly {
    sstore(slot, value) // Direct storage manipulation
    let data := sload(slot) // Direct storage read
}

// Storage collision in proxies:
contract Proxy {
    address implementation; // slot 0
    // If implementation uses slot 0, collision occurs
}

// Storage layout conflicts:
contract V1 { uint256 a; uint256 b; }
contract V2 { uint256 b; uint256 a; } // Layout changed!
```

#### Delegatecall Vulnerabilities
```solidity
// Storage context corruption:
contract Proxy {
    address owner; // slot 0
    
    function delegate(address target, bytes data) external {
        target.delegatecall(data); // target can modify 'owner'
    }
}

// Enhanced delegatecall attacks:
- Storage slot conflicts between proxy and implementation
- State variable shadowing
- Storage layout evolution issues
```

#### Self-Destruct Exploitation
```solidity
// Basic self-destruct:
contract Vulnerable {
    function destroy() external {
        selfdestruct(payable(msg.sender)); // Sends all ETH
    }
}

// Enhanced self-destruct attacks:
- Self-destruct + CREATE2 for address reuse
- Library self-destruct affecting multiple contracts
- Metamorphic contract patterns
```

#### CREATE2 Attack Patterns
```solidity
// Address prediction:
address predictedAddr = address(uint160(uint256(keccak256(abi.encodePacked(
    bytes1(0xff),
    deployer,
    salt,
    keccak256(bytecode)
)))));

// CREATE2 + self-destruct cycle:
1. Deploy contract at predicted address
2. Self-destruct the contract
3. Redeploy different contract at same address
```

#### Function Selector Collisions
```solidity
// Different functions with same selector:
function collate_propagate_storage(bytes16) external {} // 0x42966c68
function burn(uint256) external {}                      // 0x42966c68

// Enhanced selector attacks:
- Proxy function collision with implementation
- Signature collision in multi-call patterns
- Short signature attacks
```

#### Calldata Manipulation
```solidity
// Calldata length manipulation:
function vulnerable(uint256 a, uint256 b) external {
    // If calldata shorter than expected, b might be 0
}

// Enhanced calldata attacks:
- Calldata copying without length validation
- Assembly calldata manipulation
- ABI encoding edge cases
```

#### Bytecode & Opcode Attacks
```solidity
// Runtime bytecode modification:
assembly {
    // Modify contract's own bytecode
    codecopy(0x00, 0x00, codesize())
    // Manipulate copied bytecode
}

// Opcode manipulation:
- Direct opcode insertion via assembly
- Gas limit manipulation
- Stack underflow/overflow
```

### 3. Advanced Attack Scenarios

#### Metamorphic Contracts
```solidity
// Contract that can change its code:
1. Deploy factory with CREATE2
2. Factory deploys contract A at address X
3. Contract A self-destructs
4. Factory deploys contract B at same address X
// Address X now has different code!
```

#### Proxy Storage Corruption
```solidity
// Implementation overwrites proxy storage:
contract ProxyV1 {
    address implementation; // slot 0
    address admin;         // slot 1
}

contract ImplementationV1 {
    uint256 data; // slot 0 - COLLISION!
}
```

#### State Desynchronization
```solidity
// Cross-contract state inconsistency:
contract A {
    uint256 public balance = 100;
    
    function updateB() external {
        B(contractB).setBalance(balance);
        balance = 0; // A updated but B not in sync
    }
}
```

### 4. EVM-Level Exploitation Patterns

#### Storage Layout Analysis
- Verify storage slot assignments
- Check for storage collisions in inheritance
- Analyze proxy/implementation storage compatibility
- Look for packed storage vulnerabilities

#### Assembly Block Security
```solidity
assembly {
    // Dangerous patterns:
    calldatacopy(0, 0, calldatasize()) // Unchecked copy
    let result := call(gas(), target, 0, 0, 0, 0, 0)
    sstore(slot, arbitraryValue) // Direct storage write
}
```

#### CREATE2 Security Analysis
- Verify salt randomness and uniqueness
- Check for address prediction attacks  
- Analyze deployment access controls
- Look for CREATE2 + self-destruct patterns

### 5. Exploitation Validation
For each finding, verify:
- Technical feasibility at EVM level
- Storage layout understanding correctness
- Practical attack execution steps
- Economic incentives and impact assessment
- Real-world exploitability constraints

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector Category**: Which of the 25 state corruption vectors
- **EVM-Level Analysis**: Low-level technical details
- **Storage Impact**: Specific storage slots or memory affected
- **Exploitation Requirements**: Technical conditions needed
- **Bytecode Analysis**: Assembly or opcode details where relevant
- **Proof of Concept**: EVM-level demonstration
- **Remediation Strategy**: Low-level fixes and best practices

## Validation Criteria
- Confirm EVM-level exploitability through technical analysis
- Verify storage layout and assembly operations
- Ensure attack scenarios are technically feasible
- Provide concrete bytecode or assembly examples
- Focus on vulnerabilities with severe state corruption potential

## Special Analysis Targets

### High-Risk Patterns
1. **Proxy Contracts**: Implementation upgrades, storage layouts
2. **Factory Contracts**: CREATE2 usage, deployment patterns
3. **Library Contracts**: Delegatecall usage, shared state
4. **Assembly Usage**: Direct EVM operations, memory manipulation
5. **Upgrade Mechanisms**: State migration, storage compatibility

### Critical Code Patterns
```solidity
// 1. Unprotected delegatecall
function execute(address target, bytes calldata data) external {
    target.delegatecall(data); // No access control
}

// 2. Direct storage manipulation
assembly {
    sstore(0x00, caller()) // Direct slot 0 write
}

// 3. CREATE2 without access control
function deploy(bytes32 salt, bytes memory bytecode) external {
    address addr = Clones.cloneDeterministic(implementation, salt);
}

// 4. Self-destruct in libraries
library LibraryVulnerable {
    function destroy() external {
        selfdestruct(payable(msg.sender)); // Affects all users
    }
}

// 5. Function selector manipulation
fallback() external payable {
    address impl = implementation[msg.sig]; // Selector routing
    impl.delegatecall(msg.data);
}
```

### EVM Security Considerations
- Storage slot calculations and conflicts
- Memory expansion costs and corruption
- Stack depth limitations and overflow
- Bytecode size limitations and injection
- Gas limit manipulation and griefing

Focus on vulnerabilities that could lead to complete protocol compromise, arbitrary code execution, or critical state corruption that cannot be recovered from."""