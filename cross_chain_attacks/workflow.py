"""Cross-Chain & Bridge Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="cross-chain-attacks")
def factory():
    """Run cross-chain & bridge attack vectors detector."""
    return CrossChainAttacksDetector()


class CrossChainAttacksDetector(SimpleDetector):
    """Advanced detector covering 17 cross-chain & bridge attack vectors from VectorGuard Labs."""

    def get_detector_prompt(self) -> str:
        """Define the cross-chain & bridge attack vectors detection workflow."""
        return """# Cross-Chain & Bridge Attack Vectors Analysis

## Task
Perform comprehensive analysis of 17 critical cross-chain and bridge vulnerabilities that exploit inter-blockchain communication weaknesses and bridge protocol flaws.

## Target Attack Vectors

### 🔴 Critical Severity (16 vectors)
1. **Cross-Chain Message Replay Attack** - Message replay across chains
2. **Bridge Double-Spending Attack** - Double-spend via bridge manipulation
3. **Finality Attack** - Finality assumption exploitation
4. **Cross-Chain State Desynchronization** - State sync corruption
5. **L2 Withdrawal Blocking** - Layer 2 withdrawal prevention
6. **Cross-Chain Message Manipulation** - Inter-chain message tampering
7. **Bridge State Manipulation** - Bridge state corruption
8. **Cross-Chain Reentrancy Attack** - Reentrancy across chains
9. **Validator Compromise Attack** - Bridge validator compromise
10. **Mint/Burn Imbalance Attack** - Token mint/burn manipulation
11. **Cross-Chain MEV Attack** - MEV extraction across chains
12. **Wormhole Bridge Attack** - Wormhole-specific exploits
13. **Multichain Bridge Attack** - Multichain protocol exploits
14. **Hop Protocol Attack** - Hop bridge exploitation
15. **Synapse Protocol Attack** - Synapse bridge attacks
16. **Across Bridge Attack** - Across protocol exploitation

### 🟡 High Severity (1 vector)
17. **Chain ID Confusion Attack** - Chain identifier confusion

## Analysis Process

### 1. Discovery Phase
- Map cross-chain infrastructure (bridges, relayers, validators)
- Identify message passing protocols and verification mechanisms
- Locate L1/L2 communication patterns and withdrawal systems
- Find cross-chain token minting/burning contracts
- Analyze multi-chain deployment patterns and chain ID handling

### 2. Attack Vector Analysis

#### Cross-Chain Message Security
```solidity
// Message replay vulnerabilities:
contract CrossChainReceiver {
    mapping(bytes32 => bool) processedMessages;
    
    function processMessage(bytes32 messageHash, bytes calldata proof) external {
        // Vulnerable: no chain ID verification
        require(!processedMessages[messageHash], "Already processed");
        // Message can be replayed on different chains
        processedMessages[messageHash] = true;
        executeMessage(proof);
    }
}

// Chain ID confusion:
function verifySignature(bytes32 hash, bytes calldata signature) external view returns (bool) {
    // Vulnerable: no chain ID in signature
    address signer = ecrecover(hash, signature);
    return isAuthorizedSigner[signer];
    // Signature valid on all chains with same signer
}
```

#### Bridge Double-Spending
```solidity
// Lock-and-mint bridge vulnerabilities:
contract Bridge {
    mapping(uint256 => bool) withdrawalProcessed;
    
    function withdraw(uint256 amount, bytes32 txHash, bytes calldata proof) external {
        require(!withdrawalProcessed[txHash], "Already withdrawn");
        require(verifyProof(proof, txHash), "Invalid proof");
        
        // Vulnerable: same txHash can exist on multiple chains
        withdrawalProcessed[txHash] = true;
        token.mint(msg.sender, amount);
    }
}

// Finality attack:
function processDeposit(bytes32 blockHash, bytes calldata proof) external {
    require(isFinalized(blockHash), "Block not finalized");
    // Vulnerable: finality assumptions different across chains
    mintTokens(proof);
}
```

#### Cross-Chain State Synchronization
```solidity
// State desynchronization:
contract MultiChainVault {
    uint256 public totalLocked; // Should be consistent across chains
    
    function deposit(uint256 amount) external {
        totalLocked += amount; // Local state update only
        // If cross-chain sync fails, state becomes inconsistent
        sendCrossChainMessage(amount);
    }
}

// L2 withdrawal blocking:
function initiateWithdrawal(uint256 amount) external {
    require(balance[msg.sender] >= amount, "Insufficient balance");
    balance[msg.sender] -= amount;
    
    // Vulnerable: withdrawal can be blocked by validator manipulation
    submitWithdrawalToL1(amount, msg.sender);
}
```

#### Cross-Chain Reentrancy
```solidity
// Cross-chain reentrancy:
contract CrossChainDeFi {
    mapping(address => uint256) balances;
    
    function withdraw(uint256 amount, uint256 targetChain) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // Vulnerable: external call before state update
        sendCrossChainMessage(targetChain, amount, msg.sender);
        balances[msg.sender] -= amount; // State updated after cross-chain call
    }
}
```

### 3. Bridge-Specific Attack Patterns

#### Wormhole Bridge Vulnerabilities
```solidity
// Guardian signature verification:
function verifyVM(bytes calldata encodedVM) external returns (bool) {
    // Check for proper guardian signature validation
    // Look for replay protection mechanisms
    // Verify guardian set rotation security
}

// Token bridge mint/burn:
function completeTransfer(bytes memory encodedVM) external {
    // Check for proper burn verification on source chain
    // Verify mint authorization on destination chain
}
```

#### Multichain Protocol Issues
```solidity
// Router contract security:
function anySwapOut(address token, uint256 amount, uint256 chainID) external {
    // Check for proper chain ID validation
    // Verify token authenticity across chains
    // Look for router key compromise scenarios
}
```

#### Hop Protocol Analysis
```solidity
// Bonder mechanism security:
function bondWithdrawal(bytes32 transferId) external {
    // Check bonder collateral requirements
    // Verify challenge period enforcement
    // Look for bond slashing vulnerabilities
}
```

### 4. Protocol-Specific Security Analysis

#### Layer 2 Bridge Security
- Fraud proof mechanisms and challenge periods
- Validator set security and rotation
- Withdrawal queue manipulation
- Emergency pause and upgrade mechanisms

#### Optimistic Rollup Bridges
- Fault proof systems and dispute resolution
- Sequencer centralization risks
- Data availability assumptions
- Withdrawal finality guarantees

#### Arbitrary Message Bridges
- Message authentication and authorization
- Execution context preservation
- Gas limit handling across chains
- Fee manipulation attacks

### 5. Validator and Consensus Attacks

#### Validator Compromise Scenarios
```solidity
// Multi-signature bridge validators:
function validateMessage(bytes calldata message, bytes[] calldata signatures) external {
    require(signatures.length >= threshold, "Insufficient signatures");
    
    // Check for:
    - Validator key compromise
    - Collusion between validators  
    - Validator set rotation attacks
    - Economic incentive misalignment
}
```

#### Consensus Manipulation
- 51% attacks on bridge validators
- Long-range attacks on PoS bridges
- Eclipse attacks on bridge nodes
- Finality reversion exploits

### 6. Economic and MEV Attacks

#### Cross-Chain MEV
```solidity
// Cross-chain arbitrage manipulation:
function crossChainArbitrage(
    uint256 sourceChain,
    uint256 destChain, 
    uint256 amount
) external {
    // Look for:
    - Price oracle manipulation across chains
    - Front-running cross-chain transactions
    - Sandwich attacks on bridge operations
    - Cross-chain liquidation attacks
}
```

#### Mint/Burn Imbalance
```solidity
// Token supply manipulation:
contract CrossChainToken {
    mapping(uint256 => uint256) chainSupply;
    
    function burn(uint256 amount, uint256 targetChain) external {
        _burn(msg.sender, amount);
        chainSupply[block.chainid] -= amount;
        
        // Vulnerable: supply tracking inconsistencies
        // Can lead to infinite mint attacks
        sendMintMessage(targetChain, amount);
    }
}
```

### 7. Exploitation Validation
For each finding, verify:
- Cross-chain message flow and verification
- Economic feasibility across multiple chains
- Timing dependencies and finality requirements
- Validator behavior and incentive structures
- Protocol-specific implementation risks

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector Category**: Which of the 17 cross-chain vectors
- **Cross-Chain Flow Analysis**: Message paths and verification steps
- **Bridge Protocol Impact**: Specific protocol affected (Wormhole, Multichain, etc.)
- **Economic Analysis**: Multi-chain cost and profit calculations
- **Validator Requirements**: Needed validator compromise or collusion
- **Proof of Concept**: Cross-chain attack demonstration
- **Remediation Strategy**: Bridge security improvements

## Validation Criteria
- Confirm cross-chain exploitability through protocol analysis
- Verify message flow and verification mechanisms
- Ensure attack scenarios account for multi-chain complexity
- Provide concrete cross-chain exploit sequences
- Focus on vulnerabilities that could drain bridge TVL

## Critical Security Patterns

### Secure Cross-Chain Message Handling
```solidity
// Proper message verification:
function processMessage(
    bytes32 messageHash,
    uint256 sourceChain,
    bytes calldata proof
) external {
    bytes32 uniqueHash = keccak256(abi.encode(messageHash, sourceChain, block.chainid));
    require(!processed[uniqueHash], "Message already processed");
    require(verifyProof(sourceChain, proof), "Invalid proof");
    
    processed[uniqueHash] = true;
    executeMessage(proof);
}
```

### Chain ID Validation
```solidity
// Proper chain ID handling:
function verifySignature(bytes32 hash, bytes calldata signature) external view returns (bool) {
    bytes32 domainHash = keccak256(abi.encode(
        "EIP712Domain",
        block.chainid,
        address(this)
    ));
    bytes32 structHash = keccak256(abi.encode(hash, domainHash));
    address signer = ecrecover(structHash, signature);
    return isAuthorizedSigner[signer];
}
```

### Secure Bridge Operations
```solidity
// Protected mint/burn operations:
function mintFromBridge(
    address to,
    uint256 amount,
    bytes32 sourceTransactionHash,
    uint256 sourceChain
) external onlyBridge {
    bytes32 uniqueId = keccak256(abi.encode(
        sourceTransactionHash,
        sourceChain,
        to,
        amount
    ));
    require(!minted[uniqueId], "Already minted");
    require(verifyBurn(sourceChain, sourceTransactionHash, amount), "Burn not verified");
    
    minted[uniqueId] = true;
    _mint(to, amount);
}
```

Focus on vulnerabilities that could lead to bridge drainage, cross-chain double-spending, or complete protocol compromise across multiple blockchain networks."""