"""Time-Based Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="time-based-attacks")
def factory():
    """Run time-based attack vectors detector."""
    return TimeBasedAttacksDetector()


class TimeBasedAttacksDetector(SimpleDetector):
    """Advanced detector for Time-Based attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the time-based attack detection workflow."""
        return """# Time-Based Attack Vectors Analysis

## Task
Perform comprehensive analysis of 7 critical attack vectors related to time manipulation, block hash exploitation, and temporal dependencies in smart contracts.

## Target Attack Vectors

### 🔴 Critical Severity (1 vector)
1. **Enhanced Time Manipulation with Admin Features**
   - Admin-enhanced time attacks combining privileged access with time manipulation
   - Governance timing exploitation with emergency powers
   - Time-based admin backdoors and delayed execution attacks

### 🟡 High Severity (6 vectors)
2. **Time Manipulation Attack**
   - Basic timestamp manipulation by miners/validators
   - Time-dependent logic exploitation
   - Block timestamp gaming for profit

3. **Block Hash Attack**
   - Block hash prediction and manipulation
   - Randomness generation weaknesses
   - Hash-based decision exploitation

4. **Enhanced Time Attack**
   - Advanced multi-block time manipulation
   - Coordinated timestamp attacks
   - Time oracle manipulation

5. **Timestamp Manipulation**
   - Miner-controlled timestamp attacks
   - Time window exploitation
   - Deadline manipulation attacks

6. **Time-Lock Attack**
   - Timelock bypass techniques
   - Lock duration manipulation
   - Early unlock exploits

7. **Block Hash Manipulation**
   - Block hash influence attacks
   - Hash-based randomness exploitation
   - Multi-block hash prediction

## Analysis Process

### 1. Discovery Phase
- Identify all timestamp dependencies (block.timestamp, now)
- Locate block hash usage (block.blockhash, blockhash())
- Find timelock mechanisms and delayed executions
- Map time-sensitive functions (deadlines, expirations)
- Identify admin functions with time dependencies

### 2. Attack Vector Analysis

#### Critical: Admin-Enhanced Time Attacks
- Check for admin functions that modify time parameters
- Look for emergency functions bypassing time constraints
- Analyze governance proposals with time manipulation
- Verify time-based access control mechanisms
- Check for hidden time-based backdoors

#### Timestamp Manipulation Attacks
- Identify direct block.timestamp usage
- Check for timestamp comparisons (>, <, ==)
- Look for time-based state transitions
- Analyze auction/sale end conditions
- Verify time window validations

#### Block Hash Exploitation
- Find blockhash-based randomness
- Check for predictable hash usage
- Look for multi-block hash dependencies
- Analyze commit-reveal schemes
- Verify hash storage patterns

#### Timelock Vulnerabilities
- Map timelock implementations
- Check for bypass conditions
- Look for duration manipulation
- Analyze emergency unlock functions
- Verify cooldown periods

#### Time Oracle Dependencies
- Identify external time sources
- Check for oracle manipulation risks
- Look for time synchronization issues
- Analyze fallback mechanisms
- Verify time validation logic

### 3. Exploitation Scenarios

#### Miner/Validator Advantages
- 15-second timestamp manipulation window
- Block ordering control for time-based actions
- MEV extraction through time manipulation
- Sandwich attacks on time-sensitive operations

#### Multi-Block Coordination
- Long-term timestamp drift attacks
- Coordinated validator timestamp gaming
- Time-based market manipulation
- Governance timing attacks

#### Admin Privilege Escalation
- Emergency function time bypass
- Governance proposal fast-tracking
- Time-based admin rotation exploitation
- Delayed action manipulation

## Documentation Requirements

For each detected vulnerability:
- **Attack Type**: Which of the 7 time-based vectors
- **Manipulation Window**: Time range of possible manipulation
- **Profit Potential**: Economic incentive calculation
- **Attack Requirements**: Miner/validator control needed
- **Exploitation Steps**: Detailed attack sequence
- **Real-World Impact**: Practical consequences
- **Mitigation Code**: Specific fixes with examples

## Validation Criteria
- Confirm exploitability within Ethereum constraints
- Calculate realistic profit margins
- Consider MEV and validator incentives
- Provide concrete remediation code
- Focus on economically viable attacks

## Special Focus Areas

### Timestamp Dependencies
```solidity
// Vulnerable patterns:
if (block.timestamp >= saleEnd) {
    // Can be manipulated ±15 seconds
    endSale();
}

// Look for:
- Exact timestamp comparisons
- Short time windows (< 15 minutes)
- High-value time-dependent operations
```

### Block Hash Weaknesses
```solidity
// Vulnerable randomness:
uint256 random = uint256(blockhash(block.number - 1));
winner = participants[random % participants.length];

// Check for:
- Direct blockhash usage
- Predictable block number references
- Missing entropy sources
```

### Timelock Bypasses
```solidity
// Vulnerable timelock:
function emergencyWithdraw() onlyAdmin {
    // Bypasses timelock!
    token.transfer(admin, balance);
}

// Look for:
- Emergency functions without delays
- Admin overrides of time constraints
- Upgradeable timelock parameters
```

### Time Oracle Risks
```solidity
// Vulnerable oracle usage:
uint256 currentTime = timeOracle.getTime();
if (currentTime > deadline) {
    // Oracle can be manipulated
    liquidate(position);
}
```

### Admin Time Manipulation
```solidity
// Critical vulnerability:
function setEndTime(uint256 _endTime) onlyAdmin {
    // Admin can change active auction end time!
    auctionEndTime = _endTime;
}

// Check for:
- Modifiable time parameters
- Retroactive time changes
- Admin time fast-forwarding
```

### Compound Time Attacks
```solidity
// Multi-vector vulnerability:
function claimReward() {
    require(block.timestamp > vestingEnd);
    // Uses manipulable timestamp AND
    uint256 seed = uint256(blockhash(block.number - 1));
    // Weak randomness for bonus calculation
    uint256 bonus = seed % 100;
    transfer(msg.sender, reward + bonus);
}
```

Focus on identifying time-based vulnerabilities that can be exploited by miners, validators, or admins to extract value, manipulate outcomes, or bypass security constraints. Pay special attention to the critical admin-enhanced attacks that combine time manipulation with privileged access."""