"""Intent-Based & Account Abstraction Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="intent-aa-attacks")
def factory():
    """Run intent-based & account abstraction attack vectors detector."""
    return IntentAAAttacksDetector()


class IntentAAAttacksDetector(SimpleDetector):
    """Advanced detector for Intent-Based & Account Abstraction attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the intent-based & AA attack detection workflow."""
        return """# Intent-Based & Account Abstraction Attack Vectors Analysis

## Task
Perform comprehensive analysis of 9 critical attack vectors related to intent-based protocols and account abstraction (ERC-4337) implementations.

## Target Attack Vectors

### 🔴 Critical Severity (2 vectors)
1. **Account Abstraction Paymaster Exploitation** ($25M+ potential)
   - Paymaster fund drainage attacks
   - Stake manipulation and withdrawal exploits
   - Malicious paymaster deployment with backdoors

2. **Cross-Intent Dependency Attack** ($50M+ potential)
   - Intent cascade failures and atomicity violations
   - Circular dependency exploits
   - Multi-intent coordination attacks

### 🟡 High Severity (5 vectors)
3. **Intent Manipulation Attack** ($5M+ potential)
   - User intent parameter tampering
   - Solver collusion and bid manipulation
   - Intent replay and modification attacks

4. **Bundler Censorship Attack** ($2M+ potential)
   - Transaction bundler manipulation
   - Selective censorship and DoS attacks
   - Bundler MEV extraction

5. **Intent Front-Running Attack** ($3M+ potential)
   - Intent-based front-running in mempool
   - Solver front-running and sandwich attacks
   - Intent execution timing manipulation

6. **UserOperation Replay Attack** ($1M+ potential)
   - Cross-chain UserOp replay exploitation
   - Nonce manipulation and gaps
   - Expired operation replay attacks

7. **Signature Aggregation Manipulation** ($2M+ potential)
   - BLS and Schnorr signature attacks
   - Aggregated signature tampering
   - Rogue key attacks and nonce reuse

### 🟠 Medium Severity (2 vectors)
8. **Intent Solver Manipulation** ($800K+ potential)
   - Solver bid gaming and quality manipulation
   - Hidden fees and slippage exploitation
   - Coordinated solver attacks

9. **Account Abstraction Factory Exploit** ($400K+ potential)
   - Malicious account creation via factories
   - Predicted address collision attacks
   - Factory DoS and storage bloat

## Analysis Process

### 1. Discovery Phase
- Map intent protocol architecture and solver networks
- Identify ERC-4337 components (EntryPoint, Factory, Paymaster)
- Locate bundler infrastructure and mempool access
- Find signature aggregation implementations
- Analyze intent dependency graphs

### 2. Attack Vector Analysis

#### Paymaster Exploitation
- Check paymaster stake management logic
- Verify withdrawal restrictions and timelocks
- Look for unchecked withdrawTo() calls
- Analyze validatePaymasterUserOp implementations
- Check for delegatecall or selfdestruct patterns

#### Intent System Attacks
- Map intent submission and execution flow
- Check for parameter validation gaps
- Analyze solver selection mechanisms
- Verify intent atomicity guarantees
- Look for dependency manipulation vectors

#### Bundler Infrastructure
- Identify bundler endpoints and APIs
- Check for rate limiting and DoS protection
- Analyze bundle construction logic
- Look for MEV extraction opportunities
- Verify censorship resistance mechanisms

#### UserOperation Security
- Check nonce management and validation
- Verify chain ID inclusion in signatures
- Look for replay protection mechanisms
- Analyze operation expiration handling
- Check cross-chain replay vulnerabilities

#### Signature Schemes
- Identify aggregation algorithms (BLS, Schnorr)
- Check for rogue key attack protection
- Verify nonce generation randomness
- Look for signature malleability issues
- Analyze aggregation validation logic

#### Factory & Account Creation
- Check factory deployment validation
- Look for bytecode manipulation vectors
- Verify initialization protection
- Analyze CREATE2 address prediction
- Check for storage collision attacks

### 3. Exploitation Validation

For each finding, verify:
- **Attack Feasibility**: Technical requirements and constraints
- **Economic Impact**: Potential losses and attacker profits
- **Detection Difficulty**: How hidden the attack vector is
- **Mitigation Complexity**: Effort required to fix
- **Real-world Likelihood**: Probability of exploitation

## Documentation Requirements

For each detected vulnerability:
- **Vector Category**: Which of the 9 attack types
- **Component Affected**: Specific contract/system component
- **Attack Scenario**: Step-by-step exploitation path
- **Proof of Concept**: Executable attack code
- **Economic Analysis**: Cost vs profit calculation
- **Detection Method**: How to identify the attack
- **Remediation Steps**: Specific fixes and patches

## Validation Criteria
- Confirm technical exploitability with PoC
- Calculate realistic economic incentives
- Consider AA/intent protocol constraints
- Provide actionable remediation steps
- Focus on vectors with clear impact

## Special Focus Areas

### Paymaster Fund Drainage
```solidity
// Look for patterns like:
function withdrawTo(address payable withdrawAddress, uint256 amount) external {
    // Missing access control or stake checks
    withdrawAddress.transfer(amount);
}
```

### Intent Dependency Manipulation
```solidity
// Check for circular dependencies:
struct Intent {
    bytes32[] dependencies;
    // Without cycle detection
}
```

### UserOp Replay Vectors
```solidity
// Verify replay protection:
function validateUserOp(UserOperation calldata userOp) {
    // Missing chainId validation
    // No expiration checks
}
```

### Bundler MEV Extraction
```solidity
// Look for bundle ordering manipulation:
function handleOps(UserOperation[] calldata ops) {
    // No fairness guarantees
    // Arbitrary operation ordering
}
```

### Signature Aggregation Flaws
```solidity
// Check BLS implementations:
function aggregateSignatures(bytes[] calldata sigs) {
    // Missing rogue key prevention
    // No signature validation
}
```

Focus on attack vectors unique to intent-based systems and account abstraction that could lead to significant fund loss or protocol compromise."""