"""VM/ZK Proof Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="vm-zk-proof-attacks")
def factory():
    """Run VM/ZK proof attack vectors detector."""
    return VMZKProofAttacksDetector()


class VMZKProofAttacksDetector(SimpleDetector):
    """Advanced detector for VM and ZK Proof attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the VM/ZK proof attack detection workflow."""
        return """# VM/ZK Proof Attack Vectors Analysis

## Task
Perform comprehensive analysis of 8 critical attack vectors related to virtual machine exploitation and zero-knowledge proof systems including proof manipulation, prover compromise, VM instruction exploitation, and state transition attacks.

## Target Attack Vectors

### 🔴 Critical Severity (4 vectors)
1. **Prover Compromise Attack**
   - ZK circuit prover manipulation
   - Trusted setup exploitation
   - Proof generation backdoors
   - Verification key attacks

2. **Enhanced Prover Compromise**
   - Advanced prover infrastructure attacks
   - Multi-party computation exploitation
   - Coordinator node compromise
   - Distributed prover attacks

3. **State Transition Manipulation**
   - Invalid state transition proofs
   - State tree corruption
   - Rollup state attacks
   - Finality manipulation

4. **Enhanced State Transition Attack**
   - Advanced state manipulation techniques
   - Cross-layer state attacks
   - Persistent state corruption
   - State recovery prevention

### 🟡 High Severity (4 vectors)
5. **ZK Proof Manipulation**
   - Circuit constraint bypasses
   - Witness manipulation
   - Public input attacks
   - Verification bypass

6. **Enhanced ZK Proof Manipulation**
   - Advanced circuit attacks
   - Zero-knowledge soundness breaks
   - Proof aggregation exploitation
   - Recursive proof attacks

7. **VM Instruction Exploitation**
   - Virtual machine opcode attacks
   - Execution environment manipulation
   - Gas metering bypasses
   - Memory corruption attacks

8. **Enhanced VM Exploit**
   - Advanced VM instruction attacks
   - Cross-contract VM exploitation
   - VM state persistence attacks
   - Execution layer bypasses

## Analysis Process

### 1. Discovery Phase
- Map ZK circuit implementations
- Identify proof verification logic
- Locate VM instruction handlers
- Find state transition functions
- Analyze trusted setup parameters

### 2. Attack Vector Analysis

#### ZK Proof System Attacks
- Check circuit constraint completeness
- Analyze witness generation process
- Verify proof aggregation logic
- Look for soundness violations
- Test completeness guarantees

#### Prover Infrastructure Attacks
- Map prover deployment architecture
- Check trusted setup security
- Analyze coordinator vulnerabilities
- Look for key generation flaws
- Test multi-party protocols

#### VM Exploitation Techniques
- Check opcode implementations
- Analyze gas metering accuracy
- Look for memory safety issues
- Test execution isolation
- Verify state transitions

#### State Manipulation Vectors
- Map state tree structure
- Check transition validation
- Analyze finality mechanisms
- Look for rollback attacks
- Test recovery procedures

### 3. Technical Exploitation

#### Circuit Constraint Violations
- Under-constrained circuits
- Missing range checks
- Arithmetic overflow bypasses
- Field element manipulation
- Constraint system incompleteness

#### Proof Forgery Techniques
- Malicious witness generation
- Public input manipulation
- Verification key attacks
- Proof aggregation flaws
- Recursive proof exploits

#### VM Execution Attacks
- Opcode sequence exploitation
- Stack manipulation attacks
- Memory boundary violations
- Gas limit bypasses
- Execution context confusion

#### State Consistency Attacks
- Invalid state transitions
- State tree corruption
- Finality manipulation
- Rollback exploitation
- Recovery prevention

## Documentation Requirements

For each detected vulnerability:
- **Attack Category**: VM or ZK proof vector type
- **Technical Details**: Circuit/VM specific exploitation
- **Proof of Concept**: Working exploit demonstration
- **Impact Assessment**: System compromise potential
- **Mitigation Strategy**: Technical fixes required
- **Verification Method**: Security validation approach
- **Recovery Plan**: Post-attack remediation

## Validation Criteria
- Demonstrate mathematical proof breaks
- Show practical exploitation paths
- Consider cryptographic assumptions
- Provide circuit/VM fixes
- Focus on soundness violations

## Special Focus Areas

### ZK Circuit Vulnerabilities
```rust
// Under-constrained circuit example:
circuit ProofOfBalance {
    // Missing constraint allows balance manipulation
    signal private balance;
    signal private secret;
    signal public commitment;
    
    // Only checks commitment format, not balance validity
    commitment <== Poseidon([balance, secret]);
    // Missing: balance >= 0 constraint
    // Missing: balance <= MAX_BALANCE constraint
}

// Attack: Use negative balance to create false proofs
```

### Trusted Setup Compromise
```solidity
// Vulnerable setup usage:
contract ZKVerifier {
    struct VerifyingKey {
        uint256[2] alpha;
        uint256[2][2] beta;
        uint256[2][2] gamma;
        // Compromised during ceremony
    }
    
    function verifyProof(
        uint[2] memory _pA,
        uint[2][2] memory _pB,
        uint[2] memory _pC,
        uint[1] memory _pubSignals
    ) public view returns (bool) {
        // Uses compromised keys
        return Pairing.pairing(/* verification with backdoor */);
    }
}
```

### VM Opcode Exploitation
```assembly
// Malicious VM instruction sequence:
contract VMExploit {
    function exploitVM() external {
        assembly {
            // Manipulate gas metering
            let gasLeft := gas()
            
            // Exploit memory expansion cost calculation
            mstore(0x40, 0xffffffffffffffffffffffffffffffff)
            
            // Create invalid memory access
            let data := mload(add(0x40, 0x1000000))
            
            // Exploit stack underflow
            pop()
            pop()
            pop()
            
            // Return crafted data
            return(0x0, 0x20)
        }
    }
}
```

### State Transition Attack
```solidity
// Invalid state transition:
contract StateAttack {
    struct StateTransition {
        bytes32 prevStateRoot;
        bytes32 newStateRoot;
        bytes32 txHash;
        bytes proof;
    }
    
    function processTransition(StateTransition calldata transition) external {
        // Missing validation allows invalid transitions
        require(verifyProof(transition.proof), "Invalid proof");
        
        // No check that newStateRoot is valid result of applying txHash to prevStateRoot
        currentStateRoot = transition.newStateRoot;
        
        // Attacker can provide proof for any arbitrary state change
    }
}
```

### Prover Coordination Attack
```solidity
// Compromised prover network:
contract ProverNetwork {
    mapping(address => bool) public provers;
    uint256 public threshold;
    
    function submitProof(
        bytes32 stateRoot,
        bytes[] calldata proofs,
        address[] calldata signers
    ) external {
        require(signers.length >= threshold, "Insufficient signatures");
        
        // If majority of provers are compromised
        for (uint i = 0; i < signers.length; i++) {
            require(provers[signers[i]], "Invalid prover");
            // No verification that proofs are actually valid
        }
        
        // Accept malicious state root
        acceptStateRoot(stateRoot);
    }
}
```

### Enhanced Circuit Attacks
```rust
// Advanced circuit manipulation:
template MaliciousCircuit() {
    signal private input;
    signal private secret;
    signal public output;
    
    // Constraint that can be satisfied with invalid inputs
    component hasher = Poseidon(2);
    hasher.inputs[0] <== input;
    hasher.inputs[1] <== secret;
    
    // Weak constraint allows multiple valid preimages
    output <== hasher.out * 0 + 42;
    
    // Missing range checks allow field overflow attacks
    // Missing uniqueness constraints allow replay
}
```

### VM Memory Corruption
```solidity
// Memory safety violation:
contract MemoryCorruption {
    function corruptMemory() external pure {
        assembly {
            // Overwrite free memory pointer
            mstore(0x40, 0x80)
            
            // Allocate overlapping memory regions
            let ptr1 := mload(0x40)
            mstore(0x40, add(ptr1, 0x20))
            let ptr2 := mload(0x40)
            mstore(0x40, add(ptr2, 0x20))
            
            // ptr1 and ptr2 now overlap - memory corruption
            mstore(ptr1, 0xdeadbeef)
            mstore(ptr2, 0xcafebabe)
            
            // Memory now in inconsistent state
        }
    }
}
```

### Proof Aggregation Attack
```solidity
// Aggregation verification bypass:
contract ProofAggregator {
    function verifyAggregatedProof(
        bytes32[] calldata individualCommitments,
        bytes calldata aggregatedProof
    ) external view returns (bool) {
        // Flawed aggregation verification
        for (uint i = 0; i < individualCommitments.length; i++) {
            // Missing: verify each individual proof
            // Missing: check aggregation correctness
        }
        
        // Only verifies final aggregate, not components
        return verifyZKProof(aggregatedProof);
        // Attacker can aggregate invalid proofs
    }
}
```

### State Recovery Prevention
```solidity
// Persistent corruption attack:
contract StatePoisoning {
    bytes32 public stateRoot;
    mapping(bytes32 => bool) public corrupted;
    
    function poisonState(bytes32 maliciousRoot, bytes calldata proof) external {
        // Accept malicious state that cannot be recovered
        require(verifyTransitionProof(proof), "Invalid proof");
        
        // Mark current state as corrupted
        corrupted[stateRoot] = true;
        
        // Update to malicious state
        stateRoot = maliciousRoot;
        
        // Prevent rollback by corrupting history
        for (uint i = 0; i < 100; i++) {
            bytes32 historicalRoot = getHistoricalRoot(i);
            corrupted[historicalRoot] = true;
        }
    }
}
```

Focus on identifying vulnerabilities in ZK proof systems and virtual machine implementations that could compromise the cryptographic guarantees, execution integrity, or state consistency of the system. Pay special attention to soundness violations, completeness breaks, and attacks that persist beyond single transactions."""