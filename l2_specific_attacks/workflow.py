"""Layer 2 Specific Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="l2-specific-attacks")
def factory():
    """Run Layer 2 specific attack vectors detector."""
    return L2SpecificAttacksDetector()


class L2SpecificAttacksDetector(SimpleDetector):
    """Advanced detector for Layer 2 specific attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the Layer 2 specific attack detection workflow."""
        return """# Layer 2 Specific Attack Vectors Analysis

## Task
Perform comprehensive analysis of 7 critical attack vectors specific to Layer 2 scaling solutions including Optimism, Arbitrum, Polygon, StarkNet, and zkSync.

## Target Attack Vectors (All Critical Severity)

### 🔴 Critical Severity (7 vectors)
1. **Optimism Fraud Proof Attack**
   - Fraud proof challenge period exploitation
   - State root manipulation during challenge
   - Sequencer censorship attacks
   - L1-L2 message forgery

2. **Arbitrum Delayed Inbox Attack**
   - Delayed inbox message manipulation
   - Sequencer inbox bypassing
   - Force inclusion delay exploitation
   - Retryable ticket attacks

3. **Polygon Checkpoint Attack**
   - Checkpoint submission manipulation
   - Heimdall consensus attacks
   - Bor chain state corruption
   - Bridge exit fraud

4. **StarkNet L1-L2 Message Attack**
   - Cairo program verification bypass
   - L1-L2 message consumption attacks
   - State update forgery
   - STARK proof manipulation

5. **zkSync Commit Block Attack**
   - Block commitment manipulation
   - Priority queue exploitation
   - zkEVM state transition attacks
   - Proof aggregation vulnerabilities

6. **Rollup Fraud Proof Manipulation**
   - Generic fraud proof bypass techniques
   - Challenge period gaming
   - Bisection protocol exploitation
   - Validator collusion attacks

7. **Enhanced Fraud Proof Attack**
   - Advanced multi-layer fraud proof attacks
   - Cross-rollup attack vectors
   - Economic incentive manipulation
   - Time-based fraud proof exploits

## Analysis Process

### 1. Discovery Phase
- Map L2 architecture and components
- Identify fraud proof mechanisms
- Locate message passing systems
- Find state commitment processes
- Analyze economic security models

### 2. Attack Vector Analysis

#### Optimism Specific Attacks
- Check fraud proof submission and challenge logic
- Analyze 7-day challenge period vulnerabilities
- Verify L2OutputOracle state root validation
- Look for sequencer censorship resistance
- Check CrossDomainMessenger exploits

#### Arbitrum Specific Vulnerabilities
- Analyze delayed inbox implementation
- Check sequencer inbox force inclusion
- Verify retryable ticket system
- Look for challenge protocol weaknesses
- Analyze ArbOS vulnerabilities

#### Polygon Checkpoint Exploitation
- Check Heimdall checkpoint submission
- Analyze validator set management
- Verify Bor block production
- Look for bridge state synchronization issues
- Check PoS consensus vulnerabilities

#### StarkNet Attack Surfaces
- Analyze Cairo program constraints
- Check STARK proof verification
- Verify L1-L2 message consumption
- Look for sequencer manipulation
- Check state update mechanisms

#### zkSync Vulnerabilities
- Analyze block commitment process
- Check priority operation handling
- Verify zkEVM correctness proofs
- Look for proof aggregation flaws
- Check operator coordination

#### Generic Rollup Attacks
- Fraud proof timing exploitation
- Economic griefing attacks
- State transition manipulation
- Validator/sequencer collusion
- Cross-layer reentrancy

### 3. Exploitation Scenarios

#### Fraud Proof Gaming
- Submit invalid state roots before challenge deadline
- Censor fraud proof submissions
- Manipulate bisection protocol
- Exploit gas limit constraints
- Coordinate validator attacks

#### Message Passing Exploits
- Forge L1-L2 messages
- Replay messages across domains
- Manipulate message ordering
- Exploit message consumption
- Attack bridge contracts

#### Economic Attacks
- Grief challengers with high gas costs
- Manipulate token bridges for profit
- Exploit MEV in L2 context
- Attack liquidity bridges
- Manipulate fee mechanisms

## Documentation Requirements

For each detected vulnerability:
- **L2 Platform**: Specific L2 affected
- **Attack Vector**: Detailed exploitation method
- **Prerequisites**: Required conditions
- **Impact Analysis**: Funds at risk
- **Proof of Concept**: Executable attack
- **Chain-Specific Fix**: Platform-specific remediation
- **Detection Method**: Monitoring approach

## Validation Criteria
- Confirm exploitability on mainnet L2s
- Consider L2-specific constraints
- Account for economic incentives
- Provide L2-specific fixes
- Focus on critical infrastructure

## Special Focus Areas

### Optimism Fraud Proofs
```solidity
// Vulnerable pattern:
function proposeL2Output(
    bytes32 _outputRoot,
    uint256 _l2BlockNumber,
    bytes32 _l1BlockHash,
    uint256 _l1BlockNumber
) external payable {
    // Check for missing validations
    // Time constraints
    // Sequencer privileges
}

// Attack vectors:
- Race conditions in proposals
- Challenge period manipulation
- Output root forgery
```

### Arbitrum Delayed Inbox
```solidity
// Vulnerable inbox:
function forceInclusion(
    uint256 _totalDelayedMessagesRead,
    uint8 kind,
    uint256[2] calldata l1BlockAndTime,
    uint256 baseFeeL1,
    address sender,
    bytes32 messageDataHash
) external {
    // Check delay requirements
    // Verify message authenticity
}

// Exploits:
- Premature force inclusion
- Message order manipulation
- Sender spoofing
```

### Polygon Checkpoints
```solidity
// Checkpoint vulnerability:
function submitCheckpoint(
    uint256 checkpoint,
    uint256 start,
    uint256 end
) external onlyValidator {
    // Verify checkpoint validity
    // Check validator signatures
    // Ensure continuity
}

// Attack surfaces:
- Invalid checkpoint submission
- Validator set manipulation
- State root forgery
```

### StarkNet Messages
```solidity
// L1-L2 messaging flaw:
function consumeMessageFromL2(
    uint256 fromAddress,
    uint256[] calldata payload
) external {
    // Verify message hash
    // Check consumption status
    // Validate sender
}

// Vulnerabilities:
- Message replay
- Invalid consumption
- Cairo program exploits
```

### zkSync Commitments
```solidity
// Block commit vulnerability:
function commitBlocks(
    StoredBlockInfo memory _lastCommittedBlockData,
    CommitBlockInfo[] calldata _newBlocksData
) external onlyValidator {
    // Verify block data
    // Check proof requirements
    // Validate transitions
}

// Exploit paths:
- Invalid block commitments
- Proof bypassing
- State transition attacks
```

### Cross-Rollup Attacks
```solidity
// Inter-rollup vulnerability:
function relayMessage(
    address target,
    bytes calldata message,
    uint256 sourceChain
) external {
    // Missing source validation
    // No replay protection
    // Weak authentication
}

// Attack vectors:
- Cross-rollup message forgery
- State synchronization attacks
- Bridge exploitation
```

### Economic Griefing
```solidity
// Griefing vector:
function challengeStateRoot(
    uint256 blockNumber,
    bytes calldata proof
) external payable {
    require(msg.value >= challengeBond);
    // High bond enables griefing
    // Gas cost attacks
}

// Exploits:
- Challenge spam
- Gas exhaustion
- Economic DoS
```

Focus on L2-specific vulnerabilities that could compromise the entire rollup, enable fund theft, or break the trust assumptions of the scaling solution. Pay special attention to the unique security models and economic incentives of each L2 platform."""