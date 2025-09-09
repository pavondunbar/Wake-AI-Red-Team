"""Yield Farming Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="yield-farming-attacks")
def factory():
    """Run yield farming attack vectors detector."""
    return YieldFarmingAttacksDetector()


class YieldFarmingAttacksDetector(SimpleDetector):
    """Advanced detector for Yield Farming attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the yield farming attack detection workflow."""
        return """# Yield Farming Attack Vectors Analysis

## Task
Perform comprehensive analysis of 5 critical attack vectors specific to yield farming protocols including MasterChef contracts, PancakeSwap, SpiritSwap, QuickSwap farms, and Tomb Finance forks.

## Target Attack Vectors

### 🔴 Critical Severity (2 vectors)
1. **MasterChef Attack**
   - Pool manipulation and reward draining
   - Migration function exploits
   - Emergency withdraw vulnerabilities
   - Pool ID collision attacks

2. **Tomb Finance Attack**
   - Algorithmic stablecoin manipulation
   - Bond/Share price exploitation
   - Death spiral triggers
   - Boardroom governance attacks

### 🟡 High Severity (3 vectors)
3. **PancakeSwap Farm Attack**
   - CAKE token emission manipulation
   - Pool weight exploitation
   - Harvest timing attacks
   - LP token price manipulation

4. **SpiritSwap Farm Attack**
   - SPIRIT reward calculation errors
   - Boost mechanism exploitation
   - Cross-chain bridge vulnerabilities
   - Fantom-specific exploits

5. **QuickSwap Farm Attack**
   - QUICK token distribution flaws
   - Polygon bridge timing attacks
   - Dual reward exploitation
   - Dragon's Lair staking attacks

## Analysis Process

### 1. Discovery Phase
- Map farming contract architecture
- Identify reward calculation mechanisms
- Locate migration and emergency functions
- Analyze token emission schedules
- Review pool allocation logic

### 2. Attack Vector Analysis

#### MasterChef Exploitation
- Check for reentrancy in deposit/withdraw
- Analyze reward calculation precision
- Verify pool addition/update security
- Look for migration vulnerabilities
- Test emergency withdraw impacts

#### Tomb Finance Vulnerabilities
- Map algorithmic token mechanisms
- Check bond/share price calculations
- Analyze death spiral conditions
- Verify boardroom distribution logic
- Look for oracle manipulation vectors

#### PancakeSwap Specific
- Analyze CAKE emission logic
- Check pool allocation points
- Verify harvest lockup mechanisms
- Look for syrup pool exploits
- Test auto-compound vulnerabilities

#### SpiritSwap Attacks
- Check boost calculation logic
- Analyze inSpirit mechanisms
- Verify Fantom bridge security
- Look for gauge weight manipulation
- Test bribe system vulnerabilities

#### QuickSwap Exploits
- Analyze dragon's lair mechanics
- Check dual reward calculations
- Verify Polygon bridge timing
- Look for flash loan vectors
- Test liquidity mining flaws

### 3. Common Exploit Patterns

#### Reward Calculation Errors
- Integer overflow in rewards
- Precision loss exploitation
- Block time manipulation
- Reward debt miscalculation
- Pending reward drainage

#### Pool Manipulation
- Fake LP token deposits
- Pool weight gaming
- Allocation point attacks
- Pool ID collision
- Migration exploits

#### Economic Attacks
- Flash loan reward harvesting
- Sandwich attacks on deposits
- Front-running pool updates
- MEV on reward distribution
- Liquidity extraction

## Documentation Requirements

For each detected vulnerability:
- **Protocol Affected**: Specific farm implementation
- **Attack Type**: Categorized exploit method
- **Economic Impact**: TVL at risk calculation
- **Exploit Sequence**: Step-by-step attack
- **Proof of Concept**: Working exploit code
- **Fork Detection**: Similar vulnerable forks
- **Remediation**: Protocol-specific fixes

## Validation Criteria
- Test on mainnet forks
- Calculate actual profit margins
- Consider multi-pool interactions
- Verify economic viability
- Check for composability attacks

## Special Focus Areas

### MasterChef Vulnerabilities
```solidity
// Classic reentrancy:
function deposit(uint256 _pid, uint256 _amount) public {
    PoolInfo storage pool = poolInfo[_pid];
    UserInfo storage user = userInfo[_pid][msg.sender];
    
    updatePool(_pid);
    // Harvest before update - reentrancy risk!
    if (user.amount > 0) {
        uint256 pending = user.amount.mul(pool.accTokenPerShare).div(1e12).sub(user.rewardDebt);
        safeTokenTransfer(msg.sender, pending);
    }
    
    pool.lpToken.safeTransferFrom(msg.sender, address(this), _amount);
    user.amount = user.amount.add(_amount);
    user.rewardDebt = user.amount.mul(pool.accTokenPerShare).div(1e12);
}

// Exploits:
- Reentrancy through token transfers
- Reward calculation manipulation
- Pool update race conditions
```

### Migration Function Exploits
```solidity
// Vulnerable migration:
function migrate(uint256 _pid) public {
    require(address(migrator) != address(0), "no migrator");
    PoolInfo storage pool = poolInfo[_pid];
    IERC20 lpToken = pool.lpToken;
    uint256 bal = lpToken.balanceOf(address(this));
    lpToken.safeApprove(address(migrator), bal);
    IERC20 newLpToken = migrator.migrate(lpToken);
    // No validation of returned token!
    pool.lpToken = newLpToken;
}

// Attack vectors:
- Malicious migrator contract
- LP token replacement
- Balance manipulation
```

### Tomb Finance Death Spiral
```solidity
// Vulnerable bond mechanism:
function purchaseBonds(uint256 amount) external {
    require(getTombPrice() < 1e18, "Price not below peg");
    
    uint256 bondPrice = getTombPrice().mul(bondDiscount).div(100);
    uint256 bondAmount = amount.mul(1e18).div(bondPrice);
    
    tomb.burnFrom(msg.sender, amount);
    tbond.mint(msg.sender, bondAmount);
    // Death spiral: selling pressure increases discount
}

// Exploitation:
- Oracle manipulation
- Cascading liquidations
- Bond arbitrage loops
```

### Pool Weight Manipulation
```solidity
// Allocation point gaming:
function set(uint256 _pid, uint256 _allocPoint) public onlyOwner {
    massUpdatePools();
    totalAllocPoint = totalAllocPoint.sub(poolInfo[_pid].allocPoint).add(_allocPoint);
    poolInfo[_pid].allocPoint = _allocPoint;
    // Front-running opportunity!
}

// Attacks:
- Front-run allocation changes
- Sandwich pool updates
- MEV on weight changes
```

### Harvest Timing Attacks
```solidity
// Vulnerable harvest:
function harvest(uint256 _pid) public {
    PoolInfo storage pool = poolInfo[_pid];
    UserInfo storage user = userInfo[_pid][msg.sender];
    
    updatePool(_pid);
    uint256 pending = user.amount.mul(pool.accTokenPerShare).div(1e12).sub(user.rewardDebt);
    
    if (pending > 0) {
        // No cooldown check!
        rewardToken.mint(msg.sender, pending);
    }
    
    user.rewardDebt = user.amount.mul(pool.accTokenPerShare).div(1e12);
}

// Exploits:
- Rapid deposit/harvest/withdraw
- Flash loan farming
- Block stuffing attacks
```

### Dual Reward Vulnerabilities
```solidity
// Double reward calculation error:
function pendingRewards(uint256 _pid, address _user) view returns (uint256, uint256) {
    PoolInfo storage pool = poolInfo[_pid];
    UserInfo storage user = userInfo[_pid][_user];
    
    uint256 reward1 = user.amount.mul(pool.accToken1PerShare).div(1e12).sub(user.rewardDebt1);
    uint256 reward2 = user.amount.mul(pool.accToken2PerShare).div(1e12).sub(user.rewardDebt2);
    
    // Calculation mismatch can be exploited
    return (reward1, reward2);
}
```

### Emergency Withdraw Risks
```solidity
// Griefing vector:
function emergencyWithdraw(uint256 _pid) public {
    PoolInfo storage pool = poolInfo[_pid];
    UserInfo storage user = userInfo[_pid][msg.sender];
    
    uint256 amount = user.amount;
    user.amount = 0;
    user.rewardDebt = 0;
    
    // Forfeits ALL rewards - enables griefing!
    pool.lpToken.safeTransfer(msg.sender, amount);
}
```

Focus on yield farming specific vulnerabilities that can drain rewards, manipulate emissions, or break farm economics. Pay special attention to forked codebases where original vulnerabilities may persist across multiple protocols."""