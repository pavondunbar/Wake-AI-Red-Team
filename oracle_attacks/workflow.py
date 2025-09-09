"""Oracle Manipulation Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="oracle-attacks")
def factory():
    """Run oracle manipulation attack vectors detector."""
    return OracleAttacksDetector()


class OracleAttacksDetector(SimpleDetector):
    """Advanced detector covering 9 oracle manipulation attack vectors from VectorGuard Labs."""

    def get_detector_prompt(self) -> str:
        """Define the oracle manipulation attack vectors detection workflow."""
        return """# Oracle Manipulation Attack Vectors Analysis

## Task
Perform comprehensive analysis of 9 critical oracle manipulation vulnerabilities that exploit price feed dependencies, data source corruption, and oracle infrastructure weaknesses.

## Target Attack Vectors

### 🔴 Critical Severity (6 vectors)
1. **Direct Price Manipulation** - Direct oracle price manipulation
2. **Flash Loan Oracle Attack** - Flash loan + oracle combination
3. **Advanced Oracle Manipulation** - Sophisticated oracle attacks
4. **Chainlink Oracle Attack** - Chainlink-specific exploits
5. **Uniswap TWAP Attack** - TWAP oracle manipulation
6. **Oracle Price Setting** - Oracle price setting manipulation

### 🟡 High Severity (3 vectors)
7. **Tellor Oracle Attack** - Tellor protocol exploitation
8. **Band Protocol Attack** - Band oracle attacks
9. **DIA DATA Attack** - DIA oracle exploitation

## Analysis Process

### 1. Discovery Phase
- Map all oracle dependencies and price feed integrations
- Identify oracle providers (Chainlink, Uniswap TWAP, Band, Tellor, DIA)
- Locate price-dependent functions (liquidations, minting, swaps)
- Find oracle update mechanisms and validation logic
- Analyze fallback oracle implementations and circuit breakers

### 2. Attack Vector Analysis

#### Direct Price Manipulation
```solidity
// Vulnerable oracle usage:
contract VulnerableProtocol {
    IPriceOracle public oracle;
    
    function liquidate(address user) external {
        uint256 collateralPrice = oracle.getPrice(collateralToken);
        uint256 debtPrice = oracle.getPrice(debtToken);
        
        // Vulnerable: using spot price without validation
        uint256 healthFactor = calculateHealthFactor(user, collateralPrice, debtPrice);
        require(healthFactor < 1e18, "Position healthy");
        
        // Attacker can manipulate oracle to trigger liquidation
        executeLiquidation(user);
    }
    
    function mint(uint256 collateralAmount) external {
        uint256 price = oracle.getPrice(collateralToken);
        // Vulnerable: direct price usage for minting
        uint256 mintAmount = collateralAmount * price / 1e18;
        token.mint(msg.sender, mintAmount);
    }
}
```

#### Flash Loan Oracle Manipulation
```solidity
// Flash loan + oracle attack:
contract FlashLoanOracleAttack {
    function executeAttack() external {
        // Step 1: Flash loan large amount
        IFlashLoanProvider(aave).flashLoan(address(this), token, amount, "");
    }
    
    function executeOperation(
        address asset,
        uint256 amount,
        uint256 premium,
        address initiator,
        bytes calldata params
    ) external {
        // Step 2: Manipulate DEX price (affects oracle)
        IUniswapV2Router(router).swapExactTokensForTokens(
            amount,
            0,
            [asset, targetToken],
            address(this),
            block.timestamp
        );
        
        // Step 3: Exploit protocol using manipulated price
        uint256 manipulatedPrice = oracle.getPrice(targetToken);
        target.exploit(manipulatedPrice);
        
        // Step 4: Reverse manipulation
        IUniswapV2Router(router).swapExactTokensForTokens(
            profitAmount,
            0,
            [targetToken, asset],
            address(this),
            block.timestamp
        );
        
        // Step 5: Repay flash loan
        IERC20(asset).transfer(msg.sender, amount + premium);
    }
}
```

#### Chainlink Oracle Vulnerabilities
```solidity
// Chainlink price feed security issues:
contract ChainlinkOracleVulnerable {
    AggregatorV3Interface internal priceFeed;
    
    function getLatestPrice() public view returns (int) {
        (
            uint80 roundId,
            int price,
            uint startedAt,
            uint timeStamp,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        
        // Vulnerable patterns:
        // 1. No staleness check
        // 2. No price validation
        // 3. No round completeness check
        
        return price; // Dangerous without validation
    }
    
    // Secure implementation:
    function getSecurePrice() public view returns (uint256) {
        (
            uint80 roundId,
            int price,
            uint startedAt,
            uint timeStamp,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        
        // Check for stale price
        require(timeStamp > 0, "Round not complete");
        require(block.timestamp - timeStamp <= STALENESS_THRESHOLD, "Price too old");
        
        // Check for valid price
        require(price > 0, "Invalid price");
        
        // Check round ID progression
        require(answeredInRound >= roundId, "Round not answered");
        
        return uint256(price);
    }
}
```

#### Uniswap TWAP Manipulation
```solidity
// TWAP oracle manipulation:
contract TWAPManipulation {
    IUniswapV3Pool public pool;
    
    function manipulateTWAP() external {
        // TWAP manipulation techniques:
        
        // 1. Multi-block manipulation
        for (uint256 i = 0; i < MANIPULATION_BLOCKS; i++) {
            // Execute large trades to skew price
            performLargeSwap(pool, direction, amount);
            // Wait for next block
            waitForNextBlock();
        }
        
        // 2. Just-before-snapshot manipulation
        uint32[] memory secondsAgos = new uint32[](2);
        secondsAgos[0] = TWAP_PERIOD;
        secondsAgos[1] = 0;
        
        // Manipulate price right before TWAP calculation
        performLargeSwap(pool, direction, amount);
        
        // TWAP now reflects manipulated price
        (int56[] memory tickCumulatives,) = pool.observe(secondsAgos);
        int24 timeWeightedAverageTick = int24((tickCumulatives[1] - tickCumulatives[0]) / int56(uint56(TWAP_PERIOD)));
    }
}
```

#### Advanced Oracle Attack Patterns
```solidity
// Multi-oracle manipulation:
contract AdvancedOracleAttack {
    function complexAttack() external {
        // 1. Cross-oracle arbitrage manipulation
        manipulateChainlinkViaUniswap();
        
        // 2. Oracle front-running
        frontrunOracleUpdate();
        
        // 3. Sandwich oracle updates
        sandwichOracleUpdate();
        
        // 4. Multi-step oracle manipulation
        multiStepManipulation();
    }
    
    function manipulateChainlinkViaUniswap() internal {
        // If Chainlink uses Uniswap as data source
        // Manipulate Uniswap → affects Chainlink → exploit protocol
    }
    
    function frontrunOracleUpdate() internal {
        // Detect oracle update transaction in mempool
        // Front-run with position setup
        // Back-run after oracle update with profit extraction
    }
}
```

### 3. Protocol-Specific Oracle Analysis

#### Tellor Oracle Vulnerabilities
```solidity
// Tellor oracle exploitation:
contract TellorOracleAttack {
    ITellor public tellor;
    
    function attackTellor() external {
        // Tellor-specific attack vectors:
        
        // 1. Data reporter manipulation
        // - Bribe reporters to submit false data
        // - Become reporter and submit manipulated data
        
        // 2. Dispute mechanism exploitation
        // - Submit false data, wait for dispute period
        // - Front-run dispute resolution
        
        // 3. Oracle request manipulation
        // - Manipulate request parameters
        // - Time-sensitive request attacks
        
        uint256 manipulatedValue = tellor.getCurrentValue(queryId);
        exploitWithManipulatedValue(manipulatedValue);
    }
}
```

#### Band Protocol Exploitation
```solidity
// Band protocol oracle attacks:
contract BandOracleAttack {
    IStdReference public bandOracle;
    
    function attackBand() external {
        // Band-specific vulnerabilities:
        
        // 1. Validator manipulation
        // - Compromise Band validators
        // - Economic attacks on validators
        
        // 2. Data source corruption
        // - Manipulate external data sources
        // - API endpoint attacks
        
        // 3. Cross-chain oracle attacks
        // - Exploit Band's cross-chain bridges
        // - Message relay manipulation
        
        IStdReference.ReferenceData memory data = bandOracle.getReferenceData("BTC", "USD");
        exploitWithBandData(data.rate);
    }
}
```

#### DIA Oracle Vulnerabilities
```solidity
// DIA oracle exploitation:
contract DIAOracleAttack {
    IDIAOracleV2 public diaOracle;
    
    function attackDIA() external {
        // DIA-specific attack vectors:
        
        // 1. Data feed manipulation
        // - Manipulate underlying exchanges
        // - Volume-weighted average attacks
        
        // 2. Governance attacks
        // - Manipulate DIA governance
        // - Oracle parameter changes
        
        // 3. Methodological exploitation
        // - Exploit DIA's data methodology
        // - Outlier detection bypass
        
        (uint128 price, uint128 timestamp) = diaOracle.getValue("ETH/USD");
        require(timestamp > block.timestamp - MAX_STALENESS, "Stale price");
        exploitWithDIAPrice(price);
    }
}
```

### 4. Oracle Security Patterns Analysis

#### Insufficient Price Validation
```solidity
// Common vulnerable patterns:
function badOracleUsage() external {
    int price = priceFeed.latestAnswer(); // No validation
    uint256 amount = calculateAmount(uint256(price)); // Unsafe casting
}

// Secure oracle integration:
function secureOracleUsage() external {
    (
        uint80 roundId,
        int price,
        uint startedAt,
        uint timeStamp,
        uint80 answeredInRound
    ) = priceFeed.latestRoundData();
    
    require(price > 0, "Invalid price");
    require(timeStamp > 0, "Incomplete round");
    require(block.timestamp - timeStamp <= MAX_STALENESS, "Stale price");
    require(answeredInRound >= roundId, "Round not answered");
    
    uint256 validatedPrice = uint256(price);
    uint256 amount = calculateAmount(validatedPrice);
}
```

#### Circuit Breaker Analysis
```solidity
// Circuit breaker implementation:
contract OracleCircuitBreaker {
    uint256 public constant MAX_PRICE_DEVIATION = 1000; // 10%
    uint256 public lastValidPrice;
    uint256 public lastUpdateTime;
    
    function getValidatedPrice() external returns (uint256) {
        uint256 newPrice = oracle.getPrice();
        
        // Check for excessive price movement
        if (lastValidPrice > 0) {
            uint256 priceChange = newPrice > lastValidPrice 
                ? newPrice - lastValidPrice 
                : lastValidPrice - newPrice;
            uint256 percentChange = priceChange * 10000 / lastValidPrice;
            
            require(percentChange <= MAX_PRICE_DEVIATION, "Price change too large");
        }
        
        lastValidPrice = newPrice;
        lastUpdateTime = block.timestamp;
        return newPrice;
    }
}
```

### 5. Multi-Oracle Attack Scenarios

#### Oracle Arbitrage Attacks
```solidity
// Cross-oracle arbitrage:
function crossOracleArbitrage() external {
    uint256 priceA = oracleA.getPrice(token);
    uint256 priceB = oracleB.getPrice(token);
    
    if (priceA > priceB * 105 / 100) { // >5% difference
        // Exploit price discrepancy
        // 1. Use cheaper oracle for borrowing/minting
        // 2. Use expensive oracle for collateral valuation
        // 3. Profit from arbitrage
    }
}
```

#### Time-Based Oracle Attacks
```solidity
// Oracle update timing attacks:
function timingAttack() external {
    // 1. Monitor oracle update patterns
    // 2. Predict next update time
    // 3. Position before update
    // 4. Profit after update
    
    uint256 nextUpdateTime = predictNextUpdate();
    require(block.timestamp < nextUpdateTime, "Too late");
    
    setupPositionBeforeUpdate();
}
```

### 6. Exploitation Validation
For each finding, verify:
- Oracle update frequency and staleness thresholds
- Price validation mechanisms and circuit breakers
- Economic feasibility of oracle manipulation
- Multi-oracle fallback implementations
- Cross-oracle arbitrage opportunities

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector Category**: Which of the 9 oracle vectors
- **Oracle Provider Impact**: Specific oracle affected (Chainlink, TWAP, etc.)
- **Manipulation Requirements**: Conditions needed for successful attack
- **Economic Analysis**: Cost of manipulation vs. potential profit
- **Time Sensitivity**: Update frequency and staleness dependencies
- **Proof of Concept**: Oracle manipulation demonstration
- **Remediation Strategy**: Validation, circuit breakers, multi-oracle systems

## Validation Criteria
- Confirm oracle manipulation feasibility and cost
- Verify price validation mechanisms effectiveness
- Ensure attack scenarios account for oracle security measures
- Provide concrete manipulation cost calculations
- Focus on vulnerabilities with significant financial impact potential

## Critical Security Patterns

### Secure Oracle Integration
```solidity
// Multi-oracle price validation:
contract SecureOracle {
    address[] public oracles;
    uint256 public constant MAX_DEVIATION = 500; // 5%
    uint256 public constant MIN_ORACLES = 3;
    
    function getSecurePrice(address token) external view returns (uint256) {
        require(oracles.length >= MIN_ORACLES, "Insufficient oracles");
        
        uint256[] memory prices = new uint256[](oracles.length);
        uint256 validPrices = 0;
        
        // Collect prices from all oracles
        for (uint256 i = 0; i < oracles.length; i++) {
            try IPriceOracle(oracles[i]).getPrice(token) returns (uint256 price) {
                if (price > 0 && !isStale(oracles[i], token)) {
                    prices[validPrices] = price;
                    validPrices++;
                }
            } catch {
                // Oracle failed, skip
            }
        }
        
        require(validPrices >= MIN_ORACLES, "Insufficient valid prices");
        
        // Calculate median price
        uint256 medianPrice = calculateMedian(prices, validPrices);
        
        // Validate all prices are within deviation threshold
        for (uint256 i = 0; i < validPrices; i++) {
            uint256 deviation = prices[i] > medianPrice 
                ? prices[i] - medianPrice 
                : medianPrice - prices[i];
            uint256 percentDeviation = deviation * 10000 / medianPrice;
            require(percentDeviation <= MAX_DEVIATION, "Price deviation too high");
        }
        
        return medianPrice;
    }
}
```

### TWAP Security Implementation
```solidity
// Secure TWAP implementation:
contract SecureTWAP {
    uint32 public constant TWAP_PERIOD = 3600; // 1 hour
    uint32 public constant MIN_PERIOD = 600;   // 10 minutes
    
    function getSecureTWAP(address pool) external view returns (uint256) {
        uint32[] memory secondsAgos = new uint32[](2);
        secondsAgos[0] = TWAP_PERIOD;
        secondsAgos[1] = 0;
        
        (int56[] memory tickCumulatives,) = IUniswapV3Pool(pool).observe(secondsAgos);
        
        // Calculate TWAP
        int24 timeWeightedAverageTick = int24((tickCumulatives[1] - tickCumulatives[0]) / int56(uint56(TWAP_PERIOD)));
        
        // Additional validation: check shorter period TWAP for manipulation
        uint32[] memory shortPeriodAgos = new uint32[](2);
        shortPeriodAgos[0] = MIN_PERIOD;
        shortPeriodAgos[1] = 0;
        
        (int56[] memory shortTickCumulatives,) = IUniswapV3Pool(pool).observe(shortPeriodAgos);
        int24 shortTWAP = int24((shortTickCumulatives[1] - shortTickCumulatives[0]) / int56(uint56(MIN_PERIOD)));
        
        // Ensure short-term and long-term TWAPs are not too different
        int24 twapDeviation = timeWeightedAverageTick > shortTWAP 
            ? timeWeightedAverageTick - shortTWAP 
            : shortTWAP - timeWeightedAverageTick;
            
        require(uint24(twapDeviation) <= MAX_TWAP_DEVIATION, "TWAP manipulation detected");
        
        return TickMath.getSqrtRatioAtTick(timeWeightedAverageTick);
    }
}
```

Focus on vulnerabilities that could lead to significant value extraction through oracle price manipulation, protocol exploitation via false pricing, or sophisticated attacks that bypass existing oracle security mechanisms."""