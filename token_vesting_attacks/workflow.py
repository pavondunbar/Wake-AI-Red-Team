"""Token Vesting Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="token-vesting-attacks")
def factory():
    """Run token vesting attack vectors detector."""
    return TokenVestingAttacksDetector()


class TokenVestingAttacksDetector(SimpleDetector):
    """Advanced detector for Token Vesting attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the token vesting attack detection workflow."""
        return """# Token Vesting Attack Vectors Analysis

## Task
Perform comprehensive analysis of 5 high-severity attack vectors related to token vesting mechanisms including linear vesting, merkle-based vesting, time-locked vesting, Sablier streams, and LlamaPay protocol.

## Target Attack Vectors (All High Severity)

### 🟡 High Severity (5 vectors)
1. **Linear Vesting Attack**
   - Vesting calculation manipulation
   - Early unlock exploits
   - Cliff period bypasses
   - Vesting schedule manipulation

2. **Merkle Vesting Attack**
   - Merkle proof forgery
   - Double claiming exploits
   - Root update vulnerabilities
   - Allocation manipulation

3. **Time-Locked Vesting Attack**
   - Lock duration manipulation
   - Time-based unlock exploits
   - Emergency withdrawal abuse
   - Admin key vulnerabilities

4. **Sablier Stream Attack**
   - Stream rate manipulation
   - Cancellation griefing
   - Recipient address spoofing
   - Token approval exploits

5. **LlamaPay Stream Attack**
   - Payment stream interruption
   - Balance calculation errors
   - Withdrawal timing attacks
   - Protocol fee bypasses

## Analysis Process

### 1. Discovery Phase
- Map vesting contract implementations
- Identify vesting calculation logic
- Locate withdrawal mechanisms
- Find admin functions
- Analyze time dependencies

### 2. Attack Vector Analysis

#### Linear Vesting Vulnerabilities
- Check vesting formula accuracy
- Analyze cliff implementation
- Verify timestamp dependencies
- Look for calculation overflows
- Test edge case behaviors

#### Merkle Vesting Exploits
- Verify merkle proof validation
- Check claim tracking mechanisms
- Analyze root update procedures
- Look for replay attacks
- Test proof generation flaws

#### Time-Lock Mechanisms
- Check lock duration logic
- Analyze unlock conditions
- Verify admin capabilities
- Look for bypass methods
- Test emergency functions

#### Sablier Protocol Attacks
- Map stream creation process
- Check cancellation logic
- Analyze recipient validation
- Look for rate manipulation
- Test approval patterns

#### LlamaPay Vulnerabilities
- Check payment calculations
- Analyze withdrawal logic
- Verify stream continuity
- Look for fee bypasses
- Test edge case scenarios

### 3. Common Exploit Patterns

#### Vesting Calculation Errors
- Integer overflow/underflow
- Precision loss in divisions
- Incorrect time calculations
- Vesting amount manipulation
- Early withdrawal exploits

#### Access Control Flaws
- Missing permission checks
- Admin function abuse
- Beneficiary impersonation
- Contract upgrade risks
- Emergency function misuse

#### Time Manipulation
- Block timestamp gaming
- Vesting acceleration
- Lock period bypasses
- Stream interruption
- Deadline manipulation

## Documentation Requirements

For each detected vulnerability:
- **Vesting Type**: Specific implementation affected
- **Attack Method**: Detailed exploitation steps
- **Financial Impact**: Tokens at risk
- **Prerequisites**: Required conditions
- **Proof of Concept**: Working exploit
- **Remediation**: Secure implementation
- **Detection Logic**: Monitoring approach

## Validation Criteria
- Test with realistic vesting schedules
- Consider gas optimization impacts
- Verify mathematical correctness
- Account for edge cases
- Provide secure alternatives

## Special Focus Areas

### Linear Vesting Calculations
```solidity
// Vulnerable vesting calculation:
function vestedAmount() public view returns (uint256) {
    if (block.timestamp < cliffTime) return 0;
    if (block.timestamp >= vestingEnd) return totalVested;
    
    // Precision loss vulnerability
    uint256 timeVested = block.timestamp - vestingStart;
    uint256 totalTime = vestingEnd - vestingStart;
    return totalVested * timeVested / totalTime; // Integer division!
}

// Exploits:
- Precision loss accumulation
- Rounding errors
- Early withdrawal timing
- Cliff bypass attempts
```

### Merkle Claim Vulnerabilities
```solidity
// Insecure merkle claiming:
mapping(address => bool) public claimed;

function claim(uint256 amount, bytes32[] calldata proof) external {
    require(!claimed[msg.sender], "Already claimed");
    
    bytes32 leaf = keccak256(abi.encodePacked(msg.sender, amount));
    require(MerkleProof.verify(proof, root, leaf), "Invalid proof");
    
    claimed[msg.sender] = true;
    token.transfer(msg.sender, amount);
    // Missing: merkle root versioning, amount validation
}

// Attack vectors:
- Root update race conditions
- Proof reuse after root change
- Amount manipulation
- Address collision attacks
```

### Time-Lock Bypass
```solidity
// Weak time-lock implementation:
uint256 public unlockTime;
address public beneficiary;

function withdraw() external {
    require(msg.sender == beneficiary, "Not beneficiary");
    require(block.timestamp >= unlockTime, "Still locked");
    
    // Missing: partial withdrawal protection
    uint256 balance = token.balanceOf(address(this));
    token.transfer(beneficiary, balance);
}

// Vulnerabilities:
- All-or-nothing withdrawals
- No vesting schedule
- Single point of failure
- No recovery mechanisms
```

### Sablier Stream Manipulation
```solidity
// Stream vulnerability:
struct Stream {
    uint256 ratePerSecond;
    uint256 startTime;
    uint256 stopTime;
    uint256 withdrawn;
}

function withdrawFromStream(uint256 streamId, uint256 amount) external {
    Stream storage stream = streams[streamId];
    require(msg.sender == stream.recipient, "Not recipient");
    
    uint256 available = balanceOf(streamId);
    require(amount <= available, "Insufficient balance");
    
    // Race condition with cancellation!
    stream.withdrawn += amount;
    token.transfer(msg.sender, amount);
}

// Exploits:
- Cancellation race conditions
- Balance calculation errors
- Recipient spoofing
- Rate manipulation
```

### LlamaPay Balance Errors
```solidity
// Payment stream calculation flaw:
function withdrawable(address user) public view returns (uint256) {
    uint256 lastPaid = lastPaymentTime[user];
    uint256 owed = (block.timestamp - lastPaid) * paymentRate[user];
    
    // No balance check!
    return owed;
}

function withdraw() external {
    uint256 amount = withdrawable(msg.sender);
    lastPaymentTime[msg.sender] = block.timestamp;
    
    // Can exceed contract balance
    token.transfer(msg.sender, amount);
}

// Issues:
- Balance exceeding
- Rate changes not handled
- No pause mechanism
- Withdrawal front-running
```

### Multi-Beneficiary Vulnerabilities
```solidity
// Shared vesting pool risk:
mapping(address => uint256) public shares;
uint256 public totalShares;
uint256 public totalVested;

function claim() external {
    uint256 userShare = shares[msg.sender];
    require(userShare > 0, "No shares");
    
    // Global state manipulation affects all users
    uint256 claimable = totalVested * userShare / totalShares;
    shares[msg.sender] = 0;
    totalShares -= userShare;
    
    token.transfer(msg.sender, claimable);
}

// Attacks:
- Late claimer disadvantage
- Share dilution
- Front-running claims
- Dust accumulation
```

### Admin Abuse Vectors
```solidity
// Dangerous admin functions:
function updateVestingSchedule(
    address beneficiary,
    uint256 newAmount,
    uint256 newEndTime
) external onlyAdmin {
    // No restrictions on changes!
    vestingAmount[beneficiary] = newAmount;
    vestingEndTime[beneficiary] = newEndTime;
}

function emergencyWithdraw() external onlyAdmin {
    // Admin can rug all vesting tokens!
    uint256 balance = token.balanceOf(address(this));
    token.transfer(admin, balance);
}

// Risks:
- Schedule manipulation
- Fund extraction
- Beneficiary griefing
- Trust assumptions
```

Focus on identifying vulnerabilities in vesting mechanisms that could allow early token access, calculation manipulation, or unauthorized withdrawals. Pay special attention to time-based logic, mathematical precision, and access control implementations."""