"""Arithmetic/Mathematical Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="arithmetic-attacks")
def factory():
    """Run arithmetic/mathematical attack vectors detector."""
    return ArithmeticAttacksDetector()


class ArithmeticAttacksDetector(SimpleDetector):
    """Advanced detector covering 9 arithmetic/mathematical attack vectors from VectorGuard Labs."""

    def get_detector_prompt(self) -> str:
        """Define the arithmetic/mathematical attack vectors detection workflow."""
        return """# Arithmetic/Mathematical Attack Vectors Analysis

## Task
Perform comprehensive analysis of 9 critical arithmetic and mathematical vulnerabilities that exploit computational weaknesses in smart contracts.

## Target Attack Vectors

### 🔴 Critical Severity (5 vectors)
1. **Integer Overflow Attack** - Integer overflow exploitation
2. **Integer Underflow Attack** - Integer underflow exploitation  
3. **Multiplication Overflow Attack** - Multiplication overflow exploitation
4. **Enhanced Overflow Attack** - Advanced overflow techniques
5. **Share Price Calculation Manipulation** - Share price manipulation

### 🟡 High Severity (3 vectors)  
6. **Division by Zero Attack** - Zero division exploitation
7. **Precision Loss Attack** - Rounding error exploitation
8. **Enhanced Arithmetic Attack** - Complex arithmetic exploitation

### 🟠 Medium Severity (1 vector)
9. **Modulo Bias Attack** - Modulo operation bias exploitation

## Analysis Process

### 1. Discovery Phase
- Map all arithmetic operations in the codebase
- Identify unchecked math operations (especially in older Solidity versions)
- Locate price calculation mechanisms and share conversion functions
- Find division operations and potential zero denominators
- Analyze precision-sensitive calculations (tokens, percentages)

### 2. Attack Vector Analysis

#### Integer Overflow/Underflow Vulnerabilities
```solidity
// Pre-Solidity 0.8.0 patterns (unchecked math):
uint256 balance = balances[user];
balance += amount; // Potential overflow
balance -= amount; // Potential underflow

// Post-0.8.0 with unchecked blocks:
unchecked {
    balance = balance + amount; // Deliberately unchecked
}

// Multiplication overflow:
uint256 result = largeNumber * multiplier; // Check for overflow
```

#### Division by Zero Attacks
```solidity
// Direct division vulnerabilities:
uint256 result = numerator / denominator; // denominator could be 0
uint256 percentage = (amount * 100) / totalSupply; // totalSupply could be 0

// Modulo by zero:
uint256 remainder = value % divisor; // divisor could be 0
```

#### Precision Loss Exploits
```solidity
// Rounding down attacks:
uint256 fee = (amount * feeRate) / 10000; // Small amounts round to 0
uint256 reward = balance / totalParticipants; // Division truncation

// Order of operations issues:
uint256 result = (a * b) / c; // vs (a / c) * b
```

#### Share Price Manipulation
```solidity
// Vault share calculations:
uint256 shares = (amount * totalShares) / totalAssets;
uint256 assets = (shares * totalAssets) / totalShares;

// Look for:
- First depositor attacks (totalShares = 0)
- Inflation attacks via direct asset transfer
- Rounding direction favoritism
```

#### Advanced Arithmetic Exploits
```solidity
// Complex calculations vulnerable to manipulation:
function calculateRewards(uint256 principal, uint256 rate, uint256 time) external {
    uint256 compound = principal * (rate ** time) / (100 ** time);
    // Check for overflow in exponential calculations
}

// Multiple operation chains:
uint256 result = ((a * b) + c) / d - e;
// Each operation could overflow/underflow
```

### 3. Solidity Version Considerations

#### Pre-0.8.0 Analysis (High Risk)
- All arithmetic operations are unchecked
- Search for missing SafeMath usage
- Look for custom arithmetic without overflow protection

#### Post-0.8.0 Analysis  
- Focus on `unchecked` blocks
- Analyze assembly arithmetic operations
- Check for explicit overflow/underflow requirements

### 4. Exploitation Scenarios

#### First Depositor/Share Inflation Attack
```solidity
// Attack sequence:
1. Deploy vault with 1 wei deposit (gets 1 share)
2. Direct transfer large amount to vault (doesn't mint shares)
3. Share price becomes inflated: sharePrice = totalAssets / totalShares
4. Subsequent depositors get rounded down to 0 shares for small deposits
```

#### Integer Overflow Token Minting
```solidity
// Vulnerable pattern:
function mint(address to, uint256 amount) external {
    totalSupply += amount; // Could overflow
    balances[to] += amount; // Could overflow
}
```

#### Division Precision Attacks
```solidity
// Attacker manipulates to make fee calculations round to 0:
uint256 fee = (smallAmount * feeRate) / BASIS_POINTS; // = 0 due to rounding
```

### 5. Detection Patterns

#### Critical Code Patterns
```solidity
// 1. Unchecked arithmetic in older contracts
pragma solidity ^0.7.0; // or earlier
uint256 result = a + b; // No overflow protection

// 2. Explicit unchecked blocks
unchecked {
    balance = balance - amount;
}

// 3. Division without zero checks
function divide(uint256 a, uint256 b) external returns (uint256) {
    return a / b; // No zero check
}

// 4. Share/vault calculations
uint256 shares = amount.mul(totalShares).div(totalAssets);

// 5. Complex mathematical formulas
uint256 compound = principal.mul(rate.add(100).pow(time)).div(100.pow(time));
```

### 6. Exploitation Validation
For each finding, verify:
- Practical exploitability (not just theoretical overflow)
- Economic incentives for attackers
- Required conditions (contract state, timing)
- Potential financial impact
- Likelihood of successful exploitation

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector Category**: Which of the 9 arithmetic vectors
- **Severity Classification**: Based on potential financial impact
- **Mathematical Analysis**: Detailed calculation of overflow/underflow conditions
- **Exploitation Requirements**: Specific conditions needed for attack
- **Economic Impact**: Estimated funds at risk or advantage gained
- **Proof of Concept**: Mathematical demonstration with concrete values
- **Remediation Strategy**: SafeMath, checks, or algorithm improvements

## Validation Criteria
- Confirm mathematical exploitability with concrete examples
- Verify economic viability (profit exceeds gas costs)
- Ensure attack scenarios account for real-world constraints
- Provide specific numerical examples demonstrating the vulnerability
- Focus on issues that could lead to fund loss or unfair advantage

## Special Analysis Targets

### High-Risk Contract Types
1. **DeFi Vaults/Pools**: Share price calculations, deposit/withdrawal math
2. **Token Contracts**: Mint/burn arithmetic, supply calculations  
3. **Staking Rewards**: Compound interest, time-based calculations
4. **AMM/DEX**: Price calculations, liquidity math, fee computations
5. **Lending Protocols**: Interest calculations, collateral ratios
6. **Governance**: Voting power calculations, quorum thresholds

### Mathematical Complexity Indicators
- Exponential operations (a**b)
- Multiple nested arithmetic operations
- Financial calculations involving percentages
- Time-based compound calculations
- Share/asset conversion formulas
- Cross-token exchange rate calculations

Focus on vulnerabilities where mathematical precision errors or overflows could lead to significant economic advantages for attackers or loss of funds for users."""