"""Liquid Staking & Restaking Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="liquid-restaking-attacks")
def factory():
    """Run liquid staking & restaking attack vectors detector."""
    return LiquidRestakingAttacksDetector()


class LiquidRestakingAttacksDetector(SimpleDetector):
    """Advanced detector for Liquid Staking & Restaking attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the liquid staking & restaking attack detection workflow."""
        return """# Liquid Staking & Restaking Attack Vectors Analysis

## Task
Perform comprehensive analysis of 8 critical attack vectors related to liquid staking protocols and restaking mechanisms.

## Target Attack Vectors

### 🔴 Critical Severity (4 vectors)
1. **Liquid Staking Token Depeg Exploitation** ($200M+ potential)
   - Market collapse through engineered depegs
   - Oracle manipulation for mass liquidations
   - Cascading withdrawals and bank run scenarios

2. **Restaking Slashing Cascade Attack** ($100M+ potential)
   - Mass slashing event triggers
   - Cross-protocol slashing propagation
   - Validator set corruption attacks

3. **Cross-Protocol Staking Arbitrage** ($50M+ potential)
   - Multi-protocol staking reward drainage
   - Rate arbitrage exploitation
   - Circular staking attacks

4. **Validator MEV Theft Attack** ($25M+ potential)
   - Validator reward interception
   - MEV extraction manipulation
   - Block proposal theft

### 🟡 High Severity (3 vectors)
5. **Validator Set Manipulation** ($8M+ potential)
   - Validator selection gaming
   - Stake concentration attacks
   - Governance takeover via validators

6. **Liquid Staking Withdrawal Queue Attack** ($5M+ potential)
   - Queue manipulation and front-running
   - Withdrawal DoS attacks
   - Exit liquidity crises

7. **Staking Derivative Price Manipulation** ($3M+ potential)
   - LST price oracle attacks
   - Derivative arbitrage exploitation
   - Synthetic staking attacks

### 🟠 Medium Severity (1 vector)
8. **Restaking Operator Collusion** ($600K+ potential)
   - Operator coordination attacks
   - Delegation manipulation
   - Fee extraction schemes

## Analysis Process

### 1. Discovery Phase
- Map liquid staking protocol architecture
- Identify restaking mechanisms and operators
- Locate validator management systems
- Find withdrawal queue implementations
- Analyze cross-protocol dependencies

### 2. Attack Vector Analysis

#### Depeg Exploitation
- Check LST/ETH price feed mechanisms
- Analyze market making and liquidity provisions
- Look for oracle dependencies and delays
- Verify depeg protection mechanisms
- Check cascading liquidation risks

#### Slashing Cascade Attacks
- Map slashing conditions across protocols
- Check for slashing event propagation
- Analyze validator insurance mechanisms
- Look for correlated slashing risks
- Verify slashing caps and limits

#### Cross-Protocol Arbitrage
- Identify multi-protocol staking positions
- Check for circular dependencies
- Analyze reward distribution timing
- Look for rate manipulation vectors
- Verify protocol isolation

#### Validator MEV Theft
- Check block proposal mechanisms
- Analyze MEV distribution logic
- Look for reward skimming opportunities
- Verify validator authentication
- Check for proposal manipulation

#### Validator Set Control
- Analyze validator selection algorithms
- Check for stake concentration limits
- Look for validator rotation vulnerabilities
- Verify decentralization measures
- Check governance weight calculations

#### Withdrawal Queue Manipulation
- Map withdrawal request flow
- Check queue ordering logic
- Look for priority manipulation
- Analyze queue capacity limits
- Verify fair ordering guarantees

#### Derivative Price Attacks
- Identify price calculation methods
- Check for manipulation windows
- Analyze arbitrage opportunities
- Look for oracle weaknesses
- Verify price update mechanisms

#### Operator Collusion
- Map operator relationships
- Check for coordination incentives
- Analyze delegation mechanisms
- Look for fee extraction vectors
- Verify operator limits

### 3. Exploitation Validation

For each finding, verify:
- **Economic Impact**: Total value at risk
- **Attack Complexity**: Technical requirements
- **Success Probability**: Likelihood of execution
- **Detection Difficulty**: How covert the attack is
- **Systemic Risk**: Protocol-wide implications

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector**: Which of the 8 categories
- **Affected Components**: Specific contracts and systems
- **Attack Methodology**: Step-by-step exploitation
- **Economic Model**: Profit calculations and costs
- **Risk Assessment**: Probability and impact matrix
- **Mitigation Strategy**: Concrete remediation steps
- **Monitoring Approach**: Detection mechanisms

## Validation Criteria
- Confirm exploitability with economic models
- Consider Ethereum staking constraints
- Account for protocol-specific mechanisms
- Provide implementable fixes
- Focus on systemic risks

## Special Focus Areas

### LST Depeg Mechanisms
```solidity
// Look for vulnerable price feeds:
function updatePrice() external {
    // No time-weighted average
    // Direct spot price usage
    uint256 price = pool.getSpotPrice();
    setPrice(price);
}
```

### Slashing Propagation
```solidity
// Check for cascading slashing:
function slash(address validator, uint256 amount) {
    // No isolation between protocols
    for (uint i = 0; i < linkedProtocols.length; i++) {
        linkedProtocols[i].slash(validator, amount);
    }
}
```

### Withdrawal Queue Gaming
```solidity
// Verify fair queue ordering:
function requestWithdrawal(uint256 amount) {
    // Vulnerable to MEV and front-running
    withdrawalQueue.push(msg.sender, amount);
    // No randomization or commit-reveal
}
```

### MEV Extraction Points
```solidity
// Check validator reward handling:
function distributeRewards() {
    // Direct transfer without validation
    uint256 rewards = block.coinbase.balance;
    validator.transfer(rewards);
}
```

### Cross-Protocol Dependencies
```solidity
// Look for circular staking:
struct StakePosition {
    address protocol;
    uint256 amount;
    // No tracking of ultimate underlying
}
```

### Operator Coordination
```solidity
// Check for collusion vectors:
function delegateToOperator(address operator) {
    // No limits on operator concentration
    // No anti-collusion measures
    operators[operator].stake += msg.value;
}
```

Focus on attack vectors unique to liquid staking and restaking that could trigger systemic failures or enable large-scale value extraction."""