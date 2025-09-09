"""Gas/Resource Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="gas-attacks")
def factory():
    """Run gas/resource attack vectors detector."""
    return GasAttacksDetector()


class GasAttacksDetector(SimpleDetector):
    """Advanced detector covering 5 gas/resource attack vectors from VectorGuard Labs."""

    def get_detector_prompt(self) -> str:
        """Define the gas/resource attack vectors detection workflow."""
        return """# Gas/Resource Attack Vectors Analysis

## Task
Perform comprehensive analysis of 5 critical gas and resource-based attack vectors that exploit computational limitations and denial-of-service vulnerabilities in smart contracts.

## Target Attack Vectors

### 🟡 High Severity (4 vectors)
1. **Gas Limit Attack** - Gas limit exploitation
2. **Enhanced Gas Griefing Attack** - Advanced gas griefing techniques
3. **Gas Limit Manipulation** - Gas boundary attacks
4. **Stealth Gas Attack** - Hidden gas consumption patterns

### 🟠 Medium Severity (1 vector)
5. **Gas Griefing Attack** - Basic gas griefing patterns

## Analysis Process

### 1. Discovery Phase
- Map gas-intensive operations (loops, external calls, storage operations)
- Identify unbounded operations and user-controlled iterations
- Locate multi-call patterns and batch operations
- Find gas limit dependencies and block gas limit assumptions
- Analyze gas estimation and refund mechanisms

### 2. Attack Vector Analysis

#### Gas Limit Exploitation
```solidity
// Unbounded loops vulnerable to gas limit attacks:
function processAll() external {
    for (uint i = 0; i < users.length; i++) {
        // If users.length is large, this will hit gas limit
        processUser(users[i]);
    }
}

// Block gas limit assumptions:
function batchProcess(uint256[] calldata amounts) external {
    for (uint i = 0; i < amounts.length; i++) {
        // Attacker can send massive array to consume block gas limit
        transfer(amounts[i]);
    }
}
```

#### Gas Griefing Attacks
```solidity
// Basic gas griefing in multi-call:
function multicall(bytes[] calldata calls) external {
    for (uint i = 0; i < calls.length; i++) {
        (bool success,) = address(this).call(calls[i]);
        require(success, "Call failed"); // Griefing: one failure ruins batch
    }
}

// Enhanced gas griefing via external calls:
function withdraw(address recipient) external {
    uint amount = balances[msg.sender];
    balances[msg.sender] = 0;
    
    // Vulnerable: recipient can consume all gas in fallback
    (bool success,) = recipient.call{value: amount}("");
    require(success, "Transfer failed");
}
```

#### Gas Limit Manipulation
```solidity
// Gas stipend manipulation:
function safeTransfer(address to, uint amount) external {
    (bool success,) = to.call{value: amount, gas: 2300}("");
    // 2300 gas stipend can be manipulated via proxy contracts
}

// Gas estimation attacks:
function estimateGas(bytes calldata data) external view returns (uint) {
    // Attacker can craft data to manipulate gas estimates
    return gasleft();
}
```

#### Stealth Gas Attacks
```solidity
// Hidden gas consumption via storage:
contract StealthGas {
    mapping(bytes32 => uint) hidden;
    
    function innocent() external {
        // Appears cheap but actually expensive due to storage operations
        for (uint i = 0; i < 100; i++) {
            hidden[keccak256(abi.encode(i, block.timestamp))] = i;
        }
    }
}

// Memory expansion attacks:
function processData(bytes calldata data) external {
    bytes memory temp = new bytes(data.length * 1000);
    // Hidden quadratic gas cost for large data
}
```

### 3. Specific Attack Scenarios

#### DoS via Gas Limit
```solidity
// Attack scenario:
1. Contract has array of users that grows over time
2. Admin function processes all users in single transaction
3. Array grows too large → function always runs out of gas
4. Contract becomes permanently stuck

// Vulnerable pattern:
address[] public stakeholders;
function distributeRewards() external onlyOwner {
    for (uint i = 0; i < stakeholders.length; i++) {
        payable(stakeholders[i]).transfer(calculateReward(stakeholders[i]));
    }
}
```

#### Gas Griefing in Batch Operations
```solidity
// Attack scenario:
1. User submits batch transaction with multiple operations
2. Attacker crafts one operation to fail after consuming gas
3. Entire batch fails but user pays for all gas consumed
4. Repeated attacks drain user funds through gas costs

// Vulnerable batch processor:
function batchExecute(Call[] calldata calls) external payable {
    for (uint i = 0; i < calls.length; i++) {
        (bool success,) = calls[i].target.call{value: calls[i].value}(calls[i].data);
        require(success); // Griefing point
    }
}
```

#### Block Gas Limit Exploitation
```solidity
// Attack scenario:
1. Attacker identifies function that processes user-controlled array
2. Submits transaction with array size approaching block gas limit
3. Transaction consumes entire block's gas allowance
4. Other transactions cannot fit in block → network congestion
```

### 4. Gas Analysis Patterns

#### High-Risk Code Patterns
```solidity
// 1. Unbounded loops
for (uint i = 0; i < userArray.length; i++) { }

// 2. Recursive calls without depth limit
function recursive(uint depth) external {
    if (depth > 0) recursive(depth - 1);
}

// 3. External calls without gas limits
target.call(data); // No gas limit specified

// 4. Storage operations in loops
for (uint i = 0; i < n; i++) {
    storage[i] = value; // Expensive storage write
}

// 5. Memory expansion in loops
for (uint i = 0; i < bigNumber; i++) {
    bytes memory temp = new bytes(1000);
}
```

#### Gas Griefing Indicators
```solidity
// 1. Batch operations with failure propagation
require(success, "Batch failed");

// 2. External calls in critical paths
(bool success,) = user.call(data);
require(success);

// 3. Gas refund dependencies
if (gasleft() > threshold) { /* operation */ }

// 4. Gas stipend assumptions
recipient.call{gas: 2300}("");
```

### 5. Resource Exhaustion Analysis

#### Memory-Based Attacks
- Large array allocations
- Quadratic memory growth patterns
- Memory copying operations
- Dynamic array resizing

#### Storage-Based Attacks
- Unbounded storage writes
- Storage slot bloating
- State tree manipulation
- Storage refund exploitation

#### Computation-Based Attacks
- Complex mathematical operations in loops
- Cryptographic operations without bounds
- Recursive function calls
- Heavy string/bytes operations

### 6. Exploitation Validation
For each finding, verify:
- Practical exploitability under current gas limits
- Economic feasibility for attackers
- Impact on protocol availability and usability
- Potential for network-level disruption
- Cost-effectiveness of the attack

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector Category**: Which of the 5 gas/resource vectors
- **Gas Cost Analysis**: Detailed gas consumption calculations
- **DoS Impact Assessment**: Availability and usability effects
- **Attack Prerequisites**: Required conditions and resources
- **Economic Analysis**: Attack costs vs. damage potential
- **Proof of Concept**: Gas consumption demonstrations
- **Remediation Strategy**: Gas optimization and safety patterns

## Validation Criteria
- Confirm gas consumption patterns through analysis
- Verify DoS potential under realistic conditions
- Ensure attack scenarios account for current gas limits
- Provide concrete gas cost calculations
- Focus on vulnerabilities that could halt protocol operations

## Remediation Patterns

### Safe Iteration Patterns
```solidity
// Paginated processing
function processUsers(uint startIndex, uint count) external {
    uint end = startIndex + count;
    if (end > users.length) end = users.length;
    
    for (uint i = startIndex; i < end; i++) {
        processUser(users[i]);
    }
}

// Pull pattern instead of push
mapping(address => uint) public rewards;
function claimReward() external {
    uint amount = rewards[msg.sender];
    rewards[msg.sender] = 0;
    payable(msg.sender).transfer(amount);
}
```

### Gas-Safe External Calls
```solidity
// Limited gas for external calls
(bool success,) = target.call{gas: 5000}(data);
// Handle failure gracefully without requiring success

// Non-blocking batch operations
function safeBatch(Call[] calldata calls) external {
    for (uint i = 0; i < calls.length; i++) {
        try this.executeCall(calls[i]) {
            // Success handling
        } catch {
            // Log error but continue processing
        }
    }
}
```

### Gas Limit Monitoring
```solidity
// Gas limit checks
modifier gasCheck() {
    uint gasStart = gasleft();
    _;
    require(gasStart - gasleft() < maxGasPerOperation, "Gas limit exceeded");
}
```

Focus on vulnerabilities that could lead to denial of service, protocol unavailability, or economic attacks through gas manipulation."""