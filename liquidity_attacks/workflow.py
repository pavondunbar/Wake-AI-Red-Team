"""Liquidity Manipulation Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="liquidity-attacks")
def factory():
    """Run liquidity manipulation attack vectors detector."""
    return LiquidityAttacksDetector()


class LiquidityAttacksDetector(SimpleDetector):
    """Advanced detector covering 13 liquidity manipulation attack vectors from VectorGuard Labs."""

    def get_detector_prompt(self) -> str:
        """Define the liquidity manipulation attack vectors detection workflow."""
        return """# Liquidity Manipulation Attack Vectors Analysis

## Task
Perform comprehensive analysis of 13 critical liquidity manipulation vulnerabilities that exploit automated market makers (AMMs), liquidity pools, and decentralized exchange mechanisms.

## Target Attack Vectors

### 🔴 Critical Severity (9 vectors)
1. **Liquidity Lock Attack** - Liquidity locking attacks
2. **Advanced Liquidity Manipulation** - Sophisticated liquidity attacks
3. **Liquidity Drain Attack** - Complete liquidity drainage
4. **AMM Pool Manipulation** - Automated market maker exploitation
5. **Curve Pool Manipulation** - Curve protocol exploitation
6. **Balancer Vault Attack** - Balancer vault exploitation
7. **Uniswap V2 Flash Swap Attack** - Uniswap V2 flash swap exploitation
8. **Uniswap V3 Flash Attack** - Uniswap V3 flash loan attacks
9. **SushiSwap Kashi Attack** - SushiSwap Kashi exploitation
10. **Curve Meta Pool Attack** - Curve meta pool attacks

### 🟡 High Severity (3 vectors)
11. **Liquidity Sandwich Attack** - Sandwich attacks on liquidity
12. **Impermanent Loss Exploit** - Impermanent loss exploitation
13. **Slippage Manipulation Attack** - Slippage exploitation

## Analysis Process

### 1. Discovery Phase
- Map AMM integrations and liquidity pool interactions
- Identify DEX protocols used (Uniswap V2/V3, Curve, Balancer, SushiSwap)
- Locate flash loan capabilities and arbitrage mechanisms
- Find price oracle dependencies and slippage protection
- Analyze liquidity provision and withdrawal mechanisms

### 2. Attack Vector Analysis

#### AMM Pool Manipulation
```solidity
// Basic AMM price manipulation:
contract VulnerableAMM {
    function swap(uint256 amountIn, address tokenIn, address tokenOut) external {
        uint256 amountOut = getAmountOut(amountIn, tokenIn, tokenOut);
        // Vulnerable: no slippage protection
        // Large swaps can manipulate price significantly
        _swap(amountIn, amountOut, tokenIn, tokenOut);
    }
    
    function getPrice(address token) external view returns (uint256) {
        // Vulnerable: spot price can be manipulated
        return reserves[token] * 1e18 / totalLiquidity;
    }
}
```

#### Flash Loan Pool Attacks
```solidity
// Uniswap V2 flash swap exploitation:
contract FlashSwapAttack {
    function attack() external {
        // Step 1: Flash swap large amount
        IUniswapV2Pair(pair).swap(amount0, amount1, address(this), abi.encode("attack"));
    }
    
    function uniswapV2Call(address sender, uint256 amount0, uint256 amount1, bytes calldata data) external {
        // Step 2: Use borrowed funds to manipulate other protocols
        manipulateTargetProtocol(amount0);
        
        // Step 3: Profit from manipulation
        uint256 profit = extractProfit();
        
        // Step 4: Repay flash swap with fee
        uint256 amountToRepay = amount0 * 1003 / 1000; // 0.3% fee
        IERC20(token0).transfer(msg.sender, amountToRepay);
    }
}
```

#### Sandwich Attack Patterns
```solidity
// MEV sandwich attack vulnerability:
function swapExactTokensForTokens(
    uint256 amountIn,
    uint256 amountOutMin, // Vulnerable: too low slippage protection
    address[] calldata path
) external {
    // Attack sequence:
    // 1. Attacker frontruns with large buy
    // 2. Victim's transaction executes at worse price
    // 3. Attacker backrims with sell for profit
    
    uint256[] memory amounts = getAmountsOut(amountIn, path);
    require(amounts[amounts.length - 1] >= amountOutMin, "INSUFFICIENT_OUTPUT_AMOUNT");
}
```

#### Curve Pool Manipulation
```solidity
// Curve stable pool attacks:
contract CurvePoolVulnerable {
    function exchange(int128 i, int128 j, uint256 dx, uint256 min_dy) external {
        // Vulnerable: A parameter manipulation
        uint256 dy = get_dy(i, j, dx);
        require(dy >= min_dy, "Slippage");
        
        // Attack: manipulate A parameter during rebalancing
        _exchange(i, j, dx, dy);
    }
    
    function add_liquidity(uint256[2] memory amounts, uint256 min_mint_amount) external {
        // Vulnerable: imbalanced deposits can be exploited
        uint256 mint_amount = calc_token_amount(amounts, true);
        require(mint_amount >= min_mint_amount, "Slippage");
    }
}
```

#### Balancer Vault Exploitation
```solidity
// Balancer weighted pool manipulation:
contract BalancerPoolAttack {
    function flashLoan(address[] tokens, uint256[] amounts, bytes userData) external {
        // Balancer flash loan attack:
        // 1. Flash loan large amounts
        // 2. Manipulate pool weights or swap fees
        // 3. Perform profitable trades
        // 4. Repay flash loan
        
        IVault(vault).flashLoan(address(this), tokens, amounts, userData);
    }
    
    function receiveFlashLoan(
        address[] tokens,
        uint256[] amounts,
        uint256[] feeAmounts,
        bytes userData
    ) external {
        // Execute manipulation during flash loan
        manipulatePoolWeights();
        performArbitrage();
        // Repay with profits
    }
}
```

### 3. Protocol-Specific Attack Analysis

#### Uniswap V2/V3 Vulnerabilities
```solidity
// Uniswap V3 concentrated liquidity attacks:
function mint(address recipient, int24 tickLower, int24 tickUpper, uint128 amount) external {
    // Look for:
    - Just-in-time (JIT) liquidity attacks
    - Tick manipulation around large trades
    - Fee tier exploitation
    - Range order manipulation
}

// V2 flash swap callback security:
function uniswapV2Call(address sender, uint256 amount0, uint256 amount1, bytes calldata data) external {
    // Verify callback authenticity
    require(msg.sender == pair, "Unauthorized callback");
    // Check for reentrancy protection
}
```

#### Curve Protocol Analysis
```solidity
// Curve meta pool vulnerabilities:
function exchange_underlying(int128 i, int128 j, uint256 dx, uint256 min_dy) external {
    // Check for:
    - Base pool manipulation via meta pool
    - Virtual price manipulation
    - Reward token inflation attacks
    - Gauge weight manipulation
}

// Curve DAO token attacks:
function vote_for_gauge_weights(address gauge, uint256 weight) external {
    // Look for governance manipulation affecting liquidity incentives
}
```

#### SushiSwap Kashi Analysis
```solidity
// Kashi lending pool attacks:
function borrow(address to, uint256 amount) external {
    // Check for:
    - Collateral ratio manipulation
    - Interest rate model exploitation
    - Liquidation threshold attacks
    - Oracle price manipulation
}
```

### 4. Advanced Liquidity Attack Scenarios

#### Just-in-Time (JIT) Liquidity Attacks
```solidity
// JIT liquidity sandwich:
1. Detect large incoming swap transaction
2. Front-run: Add concentrated liquidity around current price
3. Victim swap executes, paying fees to attacker's liquidity
4. Back-run: Remove liquidity immediately after
```

#### Cross-Protocol Arbitrage Manipulation
```solidity
// Multi-DEX price manipulation:
function crossProtocolAttack() external {
    // 1. Flash loan from Protocol A
    // 2. Manipulate price on Protocol B
    // 3. Arbitrage between A and B
    // 4. Restore price on Protocol B
    // 5. Repay flash loan with profit
}
```

#### Impermanent Loss Exploitation
```solidity
// IL attack on LPs:
function impermanentLossAttack() external {
    // 1. Monitor large liquidity positions
    // 2. Manipulate token prices to maximize IL
    // 3. Force LP withdrawal at unfavorable ratios
    // 4. Profit from LP's impermanent loss
}
```

### 5. Liquidity Security Analysis

#### Flash Loan Integration Points
- Aave, Compound, Uniswap V2, Balancer flash loans
- Flash swap capabilities and callback security
- Atomic transaction manipulation possibilities
- Cross-protocol flash loan routing

#### Price Oracle Dependencies
- AMM spot price usage for critical functions
- Time-weighted average price (TWAP) manipulation
- External oracle vs internal pool price discrepancies
- Oracle update frequency and manipulation windows

#### Slippage Protection Analysis
- Minimum output amount validation
- Maximum price impact limits
- Deadline parameter enforcement
- Multi-hop swap protection

### 6. Exploitation Validation
For each finding, verify:
- Flash loan availability and amounts needed
- Economic profitability after fees and gas costs
- MEV bot competition and frontrunning risks
- Protocol-specific security mechanisms
- Liquidity depth requirements for successful attacks

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector Category**: Which of the 13 liquidity vectors
- **DEX Protocol Impact**: Specific AMM/DEX affected
- **Economic Analysis**: Flash loan amounts, fees, and profit calculations
- **MEV Implications**: Front-running and sandwich attack potential
- **Liquidity Requirements**: Minimum liquidity needed for attack
- **Proof of Concept**: Step-by-step attack sequence with transactions
- **Remediation Strategy**: Slippage protection, oracle improvements, circuit breakers

## Validation Criteria
- Confirm economic viability through flash loan and fee analysis
- Verify liquidity depth sufficient for meaningful manipulation
- Ensure attack scenarios account for MEV competition
- Provide concrete profit/loss calculations
- Focus on vulnerabilities that could drain significant TVL

## Critical Security Patterns

### Secure AMM Integration
```solidity
// Proper slippage protection:
function safeSwap(
    uint256 amountIn,
    uint256 amountOutMin,
    address[] calldata path,
    uint256 deadline
) external {
    require(deadline >= block.timestamp, "Transaction expired");
    
    uint256[] memory amounts = router.getAmountsOut(amountIn, path);
    uint256 expectedOut = amounts[amounts.length - 1];
    
    // Conservative slippage check (e.g., max 3% slippage)
    require(amountOutMin >= expectedOut * 97 / 100, "Excessive slippage");
    
    router.swapExactTokensForTokens(amountIn, amountOutMin, path, msg.sender, deadline);
}
```

### Flash Loan Callback Security
```solidity
// Secure flash loan callback:
function receiveFlashLoan(address asset, uint256 amount, uint256 fee, bytes calldata params) external {
    require(msg.sender == FLASH_LOAN_PROVIDER, "Unauthorized callback");
    require(asset == expectedAsset, "Unexpected asset");
    
    // Implement reentrancy protection
    require(!flashLoanActive, "Reentrancy detected");
    flashLoanActive = true;
    
    // Execute flash loan logic
    executeFlashLoanLogic(asset, amount, params);
    
    // Ensure sufficient balance for repayment
    require(IERC20(asset).balanceOf(address(this)) >= amount + fee, "Insufficient repayment");
    
    flashLoanActive = false;
}
```

### Oracle Price Protection
```solidity
// TWAP price oracle integration:
function getSecurePrice(address token) external view returns (uint256) {
    uint256 twapPrice = getTWAP(token, 3600); // 1-hour TWAP
    uint256 spotPrice = getSpotPrice(token);
    
    // Reject if spot price deviates too much from TWAP
    require(
        spotPrice <= twapPrice * 105 / 100 && 
        spotPrice >= twapPrice * 95 / 100,
        "Price manipulation detected"
    );
    
    return twapPrice;
}
```

Focus on vulnerabilities that could lead to significant liquidity drainage, MEV extraction, or manipulation of critical DeFi protocols through AMM exploitation."""