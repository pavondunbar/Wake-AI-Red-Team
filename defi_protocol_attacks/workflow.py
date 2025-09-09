"""DeFi Protocol Specific Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="defi-protocol-attacks")
def factory():
    """Run DeFi protocol specific attack vectors detector."""
    return DeFiProtocolAttacksDetector()


class DeFiProtocolAttacksDetector(SimpleDetector):
    """Advanced detector covering 8 DeFi protocol specific attack vectors from VectorGuard Labs."""

    def get_detector_prompt(self) -> str:
        """Define the DeFi protocol specific attack vectors detection workflow."""
        return """# DeFi Protocol Specific Attack Vectors Analysis

## Task
Perform comprehensive analysis of 8 critical DeFi protocol-specific vulnerabilities that exploit unique mechanisms, economic models, and implementation details of major DeFi protocols.

## Target Attack Vectors

### 🔴 Critical Severity (5 vectors)
1. **Compound Borrow Attack** - Compound lending exploitation
2. **Yearn Vault Attack** - Yearn vault manipulation
3. **Synthetix Debt Pool Attack** - Synthetix debt exploitation
4. **MakerDAO CDP Attack** - MakerDAO CDP exploitation
5. **Liquity Trove Attack** - Liquity trove manipulation

### 🟡 High Severity (3 vectors)
6. **Convex Reward Attack** - Convex reward manipulation
7. **Reflexer SAFE Attack** - Reflexer SAFE exploitation
8. **Alpaca Finance Attack** - Alpaca protocol attacks

## Analysis Process

### 1. Discovery Phase
- Map DeFi protocol integrations and dependencies
- Identify protocol-specific mechanisms (lending, vaults, synthetic assets)
- Locate economic incentive structures and reward systems
- Find governance and parameter update mechanisms
- Analyze cross-protocol interactions and composability risks

### 2. Attack Vector Analysis

#### Compound Lending Exploitation
```solidity
// Compound borrow attack patterns:
contract CompoundBorrowAttack {
    IComptroller public comptroller;
    ICToken public cToken;
    
    function borrowAttack() external {
        // Attack vectors specific to Compound:
        
        // 1. Liquidation manipulation
        // - Manipulate collateral prices to trigger liquidations
        // - Front-run liquidations for profit
        // - Collateral factor manipulation
        
        // 2. Interest rate manipulation
        // - Manipulate utilization rates
        // - Exploit interest rate model changes
        // - Time-based interest accrual attacks
        
        // 3. Market listing attacks
        // - Exploit new market listings
        // - Price oracle manipulation for new assets
        // - Supply cap exploitation
        
        // 4. Governance attacks
        // - Manipulate COMP rewards
        // - Parameter change attacks
        // - Emergency pause exploitation
        
        executeCompoundExploit();
    }
    
    function liquidationAttack(address borrower, ICToken cTokenCollateral, ICToken cTokenBorrowed, uint256 repayAmount) external {
        // Flash loan for liquidation capital
        IFlashLoanProvider(aave).flashLoan(address(this), underlying, repayAmount, "");
    }
    
    function executeOperation(address asset, uint256 amount, uint256 premium, address initiator, bytes calldata params) external {
        // Liquidate underwater position
        cTokenBorrowed.liquidateBorrow(borrower, amount, cTokenCollateral);
        
        // Seize collateral at discount
        uint256 seizedAmount = cTokenCollateral.balanceOf(address(this));
        cTokenCollateral.redeem(seizedAmount);
        
        // Profit from liquidation bonus
        // Repay flash loan
        IERC20(asset).transfer(msg.sender, amount + premium);
    }
}
```

#### Yearn Vault Exploitation
```solidity
// Yearn vault attack patterns:
contract YearnVaultAttack {
    IVault public vault;
    
    function vaultAttack() external {
        // Yearn-specific attack vectors:
        
        // 1. Strategy manipulation
        // - Exploit strategy changes
        // - Harvest timing attacks
        // - Strategy debt ratio manipulation
        
        // 2. Share price manipulation
        // - First depositor attack (inflation attack)
        // - Share dilution through direct transfers
        // - Withdrawal fee manipulation
        
        // 3. Harvest MEV
        // - Front-run harvest calls
        // - Sandwich harvest transactions
        // - Keeper reward manipulation
        
        // 4. Emergency withdrawal exploitation
        // - Exploit emergency mechanisms
        // - Strategy failure attacks
        
        executeYearnExploit();
    }
    
    function inflationAttack() external {
        // Step 1: Deposit minimal amount (1 wei)
        vault.deposit(1);
        
        // Step 2: Direct transfer large amount to vault
        IERC20(underlying).transfer(address(vault), LARGE_AMOUNT);
        
        // Step 3: Share price now inflated
        // Subsequent depositors get rounded down to 0 shares
        
        // Step 4: Withdraw inflated shares
        vault.withdraw();
    }
}
```

#### Synthetix Debt Pool Exploitation
```solidity
// Synthetix debt pool attack:
contract SynthetixDebtAttack {
    ISynthetix public synthetix;
    IDebtCache public debtCache;
    
    function debtPoolAttack() external {
        // Synthetix-specific vulnerabilities:
        
        // 1. Debt pool manipulation
        // - Manipulate debt pool size
        // - Exploit debt ratio calculations
        // - Cross-asset debt shifting
        
        // 2. Oracle front-running
        // - Front-run oracle updates
        // - Exploit delayed oracle updates
        // - Currency rate manipulation
        
        // 3. Fee pool exploitation
        // - Manipulate fee distributions
        // - Staking reward attacks
        // - Fee period exploitation
        
        // 4. Synth exchange attacks
        // - Exploit exchange fees
        // - Atomic swap manipulation
        // - Settlement period attacks
        
        executeSynthetixExploit();
    }
    
    function frontRunOracle(bytes32 currencyKey) external {
        // Monitor oracle price changes
        uint256 currentRate = synthetix.exchangeRates().rateForCurrency(currencyKey);
        
        // Detect favorable price movement
        if (willPriceIncrease(currencyKey)) {
            // Exchange before price update
            synthetix.exchange("sUSD", amount, currencyKey);
            
            // Wait for oracle update
            // Exchange back for profit
            synthetix.exchange(currencyKey, newAmount, "sUSD");
        }
    }
}
```

#### MakerDAO CDP Exploitation
```solidity
// MakerDAO CDP attack patterns:
contract MakerCDPAttack {
    IVat public vat;
    IDssCdpManager public cdpManager;
    
    function cdpAttack() external {
        // MakerDAO-specific attack vectors:
        
        // 1. Liquidation manipulation
        // - Oracle price manipulation
        // - Liquidation ratio exploitation
        // - Auction mechanism attacks
        
        // 2. Stability fee exploitation
        // - Rate accumulation attacks
        // - Fee calculation manipulation
        // - Debt ceiling exploitation
        
        // 3. Emergency shutdown attacks
        // - Exploit shutdown mechanisms
        // - Collateral recovery attacks
        // - Settlement price manipulation
        
        // 4. Governance attacks
        // - Parameter manipulation via governance
        // - DSChief hat attacks
        // - Executive spell exploitation
        
        executeMakerExploit();
    }
    
    function liquidationAttack(uint256 cdp) external {
        // Manipulate collateral price to trigger liquidation
        manipulateOraclePrice(collateralType, targetPrice);
        
        // Trigger liquidation
        vat.bark(ilk, urn, address(this));
        
        // Participate in auction
        clipper.take(id, amt, max, who, data);
    }
}
```

#### Liquity Trove Manipulation
```solidity
// Liquity trove attack patterns:
contract LiquityTroveAttack {
    ITroveManager public troveManager;
    IBorrowerOperations public borrowerOps;
    
    function troveAttack() external {
        // Liquity-specific vulnerabilities:
        
        // 1. Redemption manipulation
        // - Redemption queue attacks
        // - Redemption fee manipulation
        // - TCR manipulation for redemptions
        
        // 2. Stability pool attacks
        // - LQTY reward manipulation
        // - Liquidation gain exploitation
        // - Pool emptying attacks
        
        // 3. Recovery mode exploitation
        // - TCR manipulation
        // - Sequential liquidation attacks
        // - Collateral redistribution exploitation
        
        // 4. Bootstrap liquidation
        // - Exploit liquidation ordering
        // - Gas price manipulation
        // - Batch liquidation attacks
        
        executeLiquityExploit();
    }
    
    function redemptionAttack() external {
        // Find troves with lowest collateral ratio
        address[] memory troves = getSortedTroves();
        
        // Manipulate TCR to enable redemptions
        manipulateTCR();
        
        // Execute redemption against cheapest troves
        borrowerOps.redeemCollateral(lusdAmount, firstRedemptionHint, upperPartialRedemptionHint, lowerPartialRedemptionHint, partialRedemptionHintNICR, maxIterations, maxFee);
    }
}
```

### 3. Protocol-Specific Economic Attacks

#### Convex Reward Manipulation
```solidity
// Convex reward attack:
contract ConvexRewardAttack {
    IBooster public booster;
    IBaseRewardPool public rewardPool;
    
    function rewardAttack() external {
        // Convex-specific vulnerabilities:
        
        // 1. Reward timing attacks
        // - Exploit reward distribution timing
        // - Stake right before reward distribution
        // - Unstake right after claiming
        
        // 2. Vote escrow manipulation
        // - Exploit CVX locking mechanisms
        // - Vote weight manipulation
        // - Governance reward attacks
        
        // 3. Curve gauge manipulation
        // - Exploit Curve gauge weights
        // - Cross-protocol reward farming
        // - Bribery market exploitation
        
        executeConvexExploit();
    }
    
    function timingAttack(uint256 pid) external {
        // Monitor reward distribution timing
        uint256 nextRewardTime = getNextRewardTime(pid);
        
        // Stake just before reward distribution
        if (block.timestamp >= nextRewardTime - BUFFER_TIME) {
            booster.deposit(pid, largeAmount, true);
            
            // Claim rewards immediately after distribution
            rewardPool.getReward(address(this), true);
            
            // Unstake to minimize risk
            booster.withdraw(pid, largeAmount);
        }
    }
}
```

#### Reflexer SAFE Exploitation
```solidity
// Reflexer SAFE attack:
contract ReflexerSAFEAttack {
    ISAFEEngine public safeEngine;
    IOracleRelayer public oracleRelayer;
    
    function safeAttack() external {
        // Reflexer-specific vulnerabilities:
        
        // 1. Redemption rate manipulation
        // - PI controller exploitation
        // - Rate setter attacks
        // - Dampening parameter manipulation
        
        // 2. SAFE liquidation attacks
        // - Similar to MakerDAO but with RAI specifics
        // - Liquidation ratio manipulation
        // - Auction mechanism exploitation
        
        // 3. Governance minimization attacks
        // - Exploit governance removal process
        // - Parameter lock exploitation
        // - Ungovernance timing attacks
        
        executeReflexerExploit();
    }
}
```

#### Alpaca Finance Exploitation
```solidity
// Alpaca finance attack:
contract AlpacaFinanceAttack {
    IVault public alpacaVault;
    IWorker public worker;
    
    function alpacaAttack() external {
        // Alpaca-specific vulnerabilities:
        
        // 1. Leveraged yield farming attacks
        // - Position manipulation
        // - Liquidation timing attacks
        // - Interest rate manipulation
        
        // 2. Worker strategy exploitation
        // - Strategy implementation bugs
        // - Reward token manipulation
        // - LP token price manipulation
        
        // 3. Bounty system exploitation
        // - Liquidation bounty manipulation
        // - Reinvest bounty attacks
        // - Position health manipulation
        
        executeAlpacaExploit();
    }
}
```

### 4. Cross-Protocol Attack Scenarios

#### Compound-Yearn Integration Attack
```solidity
// Cross-protocol exploitation:
function compoundYearnAttack() external {
    // 1. Deposit into Yearn vault that uses Compound strategy
    // 2. Manipulate Compound markets to affect Yearn returns
    // 3. Exploit strategy rebalancing
    // 4. Profit from cross-protocol arbitrage
}
```

#### Flash Loan Multi-Protocol Attack
```solidity
// Multi-protocol flash loan attack:
function multiProtocolFlashAttack() external {
    // 1. Flash loan large amount
    // 2. Manipulate Compound utilization rates
    // 3. Affect Yearn strategy performance
    // 4. Exploit Synthetix debt ratios
    // 5. Profit from cascading effects
    // 6. Repay flash loan
}
```

### 5. Exploitation Validation
For each finding, verify:
- Protocol-specific economic model understanding
- Integration risks with other DeFi protocols
- Governance and parameter manipulation feasibility
- Flash loan availability for required capital
- MEV competition and front-running risks

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector Category**: Which of the 8 DeFi protocol vectors
- **Protocol Specifics**: Unique mechanisms and vulnerabilities
- **Economic Model Impact**: Effects on protocol tokenomics
- **Cross-Protocol Risks**: Composability and integration vulnerabilities
- **Parameter Dependencies**: Critical parameters that could be manipulated
- **Proof of Concept**: Protocol-specific attack demonstration
- **Remediation Strategy**: Protocol-specific security improvements

## Validation Criteria
- Confirm protocol-specific vulnerability understanding
- Verify economic attack feasibility within protocol parameters
- Ensure attack scenarios account for protocol governance mechanisms
- Provide concrete economic impact calculations
- Focus on vulnerabilities unique to each protocol's design

## Critical Security Patterns

### Compound Security Checks
```solidity
// Secure Compound integration:
function secureCompoundBorrow() external {
    // Check market listing status
    require(comptroller.markets(address(cToken)).isListed, "Market not listed");
    
    // Validate collateral factor
    (, uint256 collateralFactor) = comptroller.markets(address(cToken));
    require(collateralFactor > 0, "Invalid collateral factor");
    
    // Check supply/borrow caps
    require(cToken.totalSupply() < supplyCap, "Supply cap exceeded");
    require(cToken.totalBorrows() < borrowCap, "Borrow cap exceeded");
    
    // Execute with slippage protection
    uint256 borrowAmount = calculateSafeBorrowAmount();
    require(cToken.borrow(borrowAmount) == 0, "Borrow failed");
}
```

### Yearn Vault Security
```solidity
// Secure Yearn vault interaction:
function secureYearnDeposit(uint256 amount) external {
    // Check vault health
    require(vault.emergencyShutdown() == false, "Vault in emergency shutdown");
    
    // Validate share price
    uint256 pricePerShare = vault.pricePerShare();
    require(pricePerShare > 0, "Invalid share price");
    
    // Check for inflation attacks
    uint256 totalAssets = vault.totalAssets();
    uint256 totalSupply = vault.totalSupply();
    if (totalSupply > 0) {
        require(totalAssets > MIN_TOTAL_ASSETS, "Potential inflation attack");
    }
    
    // Deposit with slippage protection
    uint256 expectedShares = amount * totalSupply / totalAssets;
    uint256 minShares = expectedShares * (10000 - MAX_SLIPPAGE) / 10000;
    
    uint256 shares = vault.deposit(amount);
    require(shares >= minShares, "Excessive slippage");
}
```

### Multi-Protocol Risk Management
```solidity
// Cross-protocol security:
contract MultiProtocolSecurity {
    mapping(address => bool) public trustedProtocols;
    mapping(address => uint256) public protocolLimits;
    
    function secureMultiProtocolInteraction(address protocol, uint256 amount) external {
        require(trustedProtocols[protocol], "Untrusted protocol");
        require(amount <= protocolLimits[protocol], "Amount exceeds limit");
        
        // Additional protocol-specific checks
        if (protocol == COMPOUND_ADDRESS) {
            validateCompoundInteraction(amount);
        } else if (protocol == YEARN_ADDRESS) {
            validateYearnInteraction(amount);
        }
        
        // Execute interaction with monitoring
        executeWithMonitoring(protocol, amount);
    }
}
```

Focus on vulnerabilities that exploit the unique economic models, governance mechanisms, and implementation details of major DeFi protocols, potentially leading to significant value extraction or protocol manipulation."""