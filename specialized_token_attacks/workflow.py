"""Specialized Token Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="specialized-token-attacks")
def factory():
    """Run specialized token attack vectors detector."""
    return SpecializedTokenAttacksDetector()


class SpecializedTokenAttacksDetector(SimpleDetector):
    """Advanced detector for Specialized Token attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the specialized token attack detection workflow."""
        return """# Specialized Token Attack Vectors Analysis

## Task
Perform comprehensive analysis of 6 high-severity attack vectors related to non-standard token implementations including fee-on-transfer, rebasing, pausable, blacklisted, deflationary, and other non-standard ERC20 tokens.

## Target Attack Vectors (All High Severity)

### 🟡 High Severity (6 vectors)
1. **Fee-on-Transfer Token Manipulation**
   - Transfer amount discrepancy exploitation
   - Fee calculation vulnerabilities
   - Double-fee extraction attacks
   - DEX integration failures

2. **Rebasing Token Manipulation**
   - Balance fluctuation attacks
   - Share/token conversion exploits
   - Oracle price manipulation
   - Liquidity pool imbalances

3. **Pausable Token Attack**
   - Pause mechanism DoS attacks
   - Emergency pause exploitation
   - Unpause race conditions
   - Locked fund scenarios

4. **Blacklist Token Attack**
   - Blacklist bypass techniques
   - Front-running blacklist additions
   - Griefing through blacklisting
   - Contract fund trapping

5. **Deflationary Token Attack**
   - Burn mechanism exploitation
   - Supply manipulation attacks
   - Reflection token vulnerabilities
   - Auto-liquidity exploits

6. **Non-Standard Token Attack**
   - Missing return value exploits
   - Non-compliant transfer behaviors
   - Approval race conditions
   - Decimal manipulation attacks

## Analysis Process

### 1. Discovery Phase
- Identify token implementation patterns
- Check for non-standard behaviors
- Map special token features
- Analyze integration points
- Review token economics

### 2. Attack Vector Analysis

#### Fee-on-Transfer Exploitation
- Check transfer hook implementations
- Analyze fee calculation logic
- Verify actual vs expected amounts
- Look for fee bypass methods
- Test DEX/AMM integrations

#### Rebasing Token Vulnerabilities
- Map rebase trigger mechanisms
- Check balance calculation methods
- Analyze share-to-token conversions
- Verify price oracle dependencies
- Test time-based rebase attacks

#### Pausable Token Risks
- Identify pause/unpause permissions
- Check for centralization risks
- Analyze pause impact on protocols
- Look for griefing opportunities
- Verify emergency procedures

#### Blacklist Mechanism Flaws
- Map blacklist update functions
- Check for admin abuse potential
- Analyze trapped fund scenarios
- Look for bypass techniques
- Verify compliance implementations

#### Deflationary Token Issues
- Analyze burn mechanisms
- Check reflection distributions
- Verify auto-liquidity logic
- Look for supply manipulation
- Test economic edge cases

#### Non-Standard Behaviors
- Check return value handling
- Verify ERC20 compliance
- Analyze approval mechanisms
- Look for reentrancy risks
- Test edge case behaviors

### 3. Integration Attack Scenarios

#### DEX/AMM Exploits
- Incorrect reserve calculations
- Slippage manipulation
- Liquidity extraction
- Price impact attacks
- K-value manipulation

#### Lending Protocol Attacks
- Collateral value manipulation
- Interest calculation errors
- Liquidation failures
- Oracle price exploits
- Borrow/supply imbalances

#### Staking/Farming Vulnerabilities
- Reward calculation errors
- Stake amount manipulation
- Harvest timing attacks
- Pool share dilution
- Exit scam vectors

## Documentation Requirements

For each detected vulnerability:
- **Token Type**: Specific token category affected
- **Attack Vector**: Detailed exploitation method
- **Integration Impact**: Affected protocols/DEXs
- **Economic Analysis**: Profit/loss calculations
- **Proof of Concept**: Working exploit code
- **Remediation**: Integration-safe practices
- **Detection Logic**: Monitoring approach

## Validation Criteria
- Test with real token implementations
- Verify on mainnet forks
- Consider gas costs
- Measure economic impact
- Provide integration guidelines

## Special Focus Areas

### Fee-on-Transfer Vulnerabilities
```solidity
// Vulnerable integration:
function swapTokens(address token, uint256 amount) external {
    IERC20(token).transferFrom(msg.sender, address(this), amount);
    // Assumes amount received = amount sent
    uint256 amountOut = calculateOutput(amount); // Wrong!
    outputToken.transfer(msg.sender, amountOut);
}

// Attack patterns:
- Input/output amount mismatches
- Double fee charging
- Sandwich attacks on fees
- Fee accumulation exploits
```

### Rebasing Token Exploits
```solidity
// Vulnerable staking:
mapping(address => uint256) public stakedAmount;

function stake(uint256 amount) external {
    token.transferFrom(msg.sender, address(this), amount);
    stakedAmount[msg.sender] += amount; // Breaks with rebasing!
}

// Vulnerabilities:
- Stale balance tracking
- Share calculation errors
- Rebase timing attacks
- Oracle manipulation
```

### Pausable Token Risks
```solidity
// Griefing vector:
function liquidate(address user) external {
    // If token is paused, liquidation fails
    collateralToken.transfer(liquidator, collateral);
    // User's position becomes unliquidatable
}

// Attack scenarios:
- Pause during liquidations
- Lock user funds
- Break protocol invariants
- DoS critical functions
```

### Blacklist Bypasses
```solidity
// Vulnerable pattern:
function deposit(uint256 amount) external {
    token.transferFrom(msg.sender, address(this), amount);
    // User gets blacklisted after deposit
    deposits[msg.sender] += amount;
    // Funds become unwithdrawable
}

// Exploits:
- Front-run blacklisting
- Trap funds in contracts
- Bypass through proxies
- Grief protocol users
```

### Deflationary Token Attacks
```solidity
// Calculation errors:
uint256 balanceBefore = token.balanceOf(address(this));
token.transferFrom(user, address(this), amount);
uint256 received = token.balanceOf(address(this)) - balanceBefore;
// received < amount due to burn!

// Issues:
- Burn on transfer
- Reflection distributions
- Auto-liquidity triggers
- Supply manipulations
```

### Non-Standard Token Traps
```solidity
// Missing return value:
interface BadToken {
    function transfer(address to, uint256 amount) external; // No return!
}

// Vulnerable usage:
require(token.transfer(recipient, amount), "Transfer failed"); // Reverts!

// Problems:
- USDT/BNB don't return bool
- Approval race conditions
- Non-standard decimals
- Transfer hooks
```

### Integration Best Practices
```solidity
// Safe integration pattern:
uint256 balanceBefore = token.balanceOf(address(this));
token.safeTransferFrom(msg.sender, address(this), amount);
uint256 actualReceived = token.balanceOf(address(this)) - balanceBefore;

// Use actualReceived for all calculations
// Never assume transfer amount = received amount
// Always check token behaviors before integration
```

Focus on identifying vulnerabilities arising from non-standard token behaviors that break common assumptions in DeFi protocols. Pay special attention to integration failures that could lead to fund loss, incorrect accounting, or protocol insolvency."""