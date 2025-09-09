"""Core Attack Mechanisms detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="core-attacks")
def factory():
    """Run core attack mechanisms detector."""
    return CoreAttackMechanismsDetector()


class CoreAttackMechanismsDetector(SimpleDetector):
    """Advanced detector covering 22 core attack mechanisms from VectorGuard Labs."""

    def get_detector_prompt(self) -> str:
        """Define the core attack mechanisms detection workflow."""
        return """# Core Attack Mechanisms Analysis

## Task
Perform comprehensive analysis of 22 critical attack mechanisms that form the foundation of smart contract exploits.

## Target Attack Vectors

### 🔴 Critical Severity (15 vectors)
1. **Advanced Flash Loan Actions** - Sophisticated flash loan manipulation techniques
2. **MEV Attack Preparation** - Maximal extractable value preparation attacks
3. **Cross-Chain Balance Manipulation** - Balance manipulation across chains
4. **L2 Bridge State Manipulation** - Layer 2 bridge state corruption
5. **Cross-Chain Message Processing** - Inter-chain message exploitation
6. **Share Price Manipulation** - Asset share price manipulation
7. **Share-to-Asset Conversion Manipulation** - Conversion rate manipulation
8. **Admin Takeover Scheduling** - Scheduled admin privilege escalation
9. **Configuration Backdoor Updates** - Hidden configuration manipulation
10. **Fake Merkle Root Setting** - Fraudulent merkle tree manipulation
11. **Merkle Proof Verification Bypass** - Merkle proof circumvention
12. **Uniswap V4 Hook Manipulation** - Uniswap V4 hook exploitation

### 🟡 High Severity (8 vectors)
13. **Signature Verification Manipulation** - Signature scheme bypass
14. **Signer Address Manipulation** - Signer identity manipulation
15. **Reward Processing Manipulation** - Reward distribution exploitation
16. **Wallet Migration Manipulation** - Wallet migration attacks
17. **Account Abstraction Targeting** - Account abstraction exploitation
18. **Account Execution Manipulation** - Account execution attacks
19. **Honeypot Activation Threshold Manipulation** - Honeypot trigger manipulation
20. **Cryptographic Operation Manipulation** - Cryptographic primitive attacks

### 🟠 Medium Severity (2 vectors)
21. **Event Emission Manipulation** - Event logging manipulation
22. **Gas Usage Optimization Exploitation** - Gas optimization bypass

## Analysis Process

### 1. Discovery Phase
- Map contract architecture and dependencies
- Identify flash loan integration points
- Locate cross-chain bridges and message passing
- Find administrative functions and upgrade mechanisms
- Analyze tokenomics and price calculation mechanisms

### 2. Attack Vector Analysis

#### Flash Loan & MEV Attacks
- Search for flash loan providers (Aave, Balancer, dYdX)
- Check for atomic arbitrage opportunities  
- Identify sandwich attack vectors in AMMs
- Look for liquidation frontrunning opportunities
- Analyze MEV protection mechanisms

#### Cross-Chain Attack Vectors
- Verify bridge security (lock/mint, burn/unlock patterns)
- Check message authentication between chains
- Look for replay attacks in cross-chain messaging
- Analyze chain reorganization handling
- Verify finality assumptions

#### Price & Share Manipulation
- Identify price oracle dependencies
- Check for flash loan price manipulation
- Analyze share/asset conversion formulas
- Look for rounding errors in calculations
- Verify slippage protection mechanisms

#### Administrative Attacks
- Map admin roles and permissions
- Check for timelock bypasses
- Look for emergency pause abuse
- Analyze upgrade patterns and backdoors
- Verify multi-sig implementations

#### Cryptographic Attacks
- Check signature verification logic
- Look for nonce reuse vulnerabilities
- Verify merkle tree implementations
- Analyze hash collision resistance
- Check random number generation

#### Account Abstraction Attacks
- Verify user operation validation
- Check for signature replay attacks
- Look for paymaster manipulation
- Analyze factory contract security
- Verify entry point implementations

#### Specialized Protocol Attacks
- **Uniswap V4**: Hook manipulation, fee bypasses
- **Layer 2**: Bridge state corruption, fraud proofs
- **Honeypots**: Activation thresholds, exit conditions

### 3. Exploitation Validation
For each finding, verify:
- Economic viability (profit > gas costs)
- Technical feasibility (contract interactions)
- Timing requirements (block dependencies)
- Capital requirements (flash loan availability)
- Risk assessment (detection probability)

## Documentation Requirements

For each detected vulnerability:
- **Attack Category**: Which of the 22 core mechanisms
- **Severity Justification**: Based on funds at risk and exploitability
- **Attack Prerequisites**: Required conditions and resources
- **Economic Analysis**: Profit calculation and capital requirements
- **Technical Exploit**: Step-by-step attack sequence
- **Proof of Concept**: Executable Solidity exploit code
- **Mitigation Strategy**: Specific remediation steps

## Validation Criteria
- Confirm exploitability through technical analysis
- Verify economic incentives exceed attack costs
- Ensure attack scenarios are realistic (not theoretical)
- Provide concrete remediation recommendations
- Focus on high-impact vulnerabilities with clear exploit paths

## Special Focus Areas

### Flash Loan Integration Points
```solidity
// Look for patterns like:
contract.flashLoan(amount, data);
// Without proper reentrancy protection
```

### Cross-Chain Message Validation
```solidity
// Check for insufficient validation:
processMessage(bytes calldata message, bytes calldata proof)
// Without proper signature/merkle verification
```

### Price Oracle Manipulation
```solidity
// Identify vulnerable price feeds:
uint256 price = oracle.getPrice(token);
// Used directly in financial calculations
```

### Administrative Function Security
```solidity
// Look for unprotected admin functions:
function setConfig(bytes calldata data) external onlyOwner
// Without timelock or multi-sig protection
```

Focus on attack vectors that could lead to significant fund loss, protocol disruption, or governance compromise."""