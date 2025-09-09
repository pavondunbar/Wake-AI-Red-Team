"""Advanced/Compound Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="advanced-compound-attacks")
def factory():
    """Run advanced/compound attack vectors detector."""
    return AdvancedCompoundAttacksDetector()


class AdvancedCompoundAttacksDetector(SimpleDetector):
    """Advanced detector for compound and multi-vector attack patterns."""

    def get_detector_prompt(self) -> str:
        """Define the advanced/compound attack detection workflow."""
        return """# Advanced/Compound Attack Vectors Analysis

## Task
Perform comprehensive analysis of 9 critical compound attack vectors that combine multiple vulnerabilities to achieve system-wide exploitation, cascading failures, and complete protocol compromise.

## Target Attack Vectors (All Critical Severity)

### 🔴 Critical Severity (9 vectors)
1. **Multi-Vector Simultaneous Attack**
   - Coordinated exploitation of multiple vulnerabilities
   - Parallel attack execution across different components
   - Synchronized timing to maximize impact
   - Defense evasion through complexity

2. **Cascading Failure Attack**
   - Triggering chain reactions of failures
   - Exploiting interdependencies between protocols
   - Amplifying small vulnerabilities into system collapse
   - Cross-protocol contagion effects

3. **System-Wide Corruption Attack**
   - Complete state corruption across all components
   - Persistent backdoor installation
   - Global invariant violations
   - Recovery prevention mechanisms

4. **Emergency Drain Attack**
   - Exploiting emergency functions for fund extraction
   - Combining admin privileges with technical vulnerabilities
   - Bypassing time locks and safeguards
   - Total value locked (TVL) extraction

5. **Governance Emergency Attack**
   - Emergency proposal exploitation
   - Combining voting manipulation with execution flaws
   - Fast-track malicious upgrades
   - Protocol takeover through governance

6. **Randomized Attack Pattern**
   - Non-deterministic attack sequences
   - Adaptive exploitation based on responses
   - Machine learning-driven attack optimization
   - Detection evasion through randomization

7. **Phased Attack Execution**
   - Multi-stage attacks with dormant periods
   - Time-delayed exploit activation
   - Building trust before exploitation
   - Long-term persistent threats

8. **Targeted Attack Sequences**
   - Custom attack chains for specific protocols
   - Exploiting unique protocol combinations
   - Precision targeting of high-value positions
   - Minimal footprint maximum impact

9. **Complete Attack Suite Execution**
   - Deployment of all available attack vectors
   - Overwhelming defenses through volume
   - Exploiting response fatigue
   - Total protocol annihilation

## Analysis Process

### 1. Attack Composition Analysis
- Map all individual vulnerabilities
- Identify exploitable combinations
- Calculate compound impact potential
- Design attack choreography
- Assess defense capabilities

### 2. Compound Attack Patterns

#### Simultaneous Multi-Vector Exploitation
- Identify parallel execution opportunities
- Map resource requirements
- Calculate timing windows
- Design coordination mechanisms
- Assess cumulative impact

#### Cascade Effect Engineering
- Map protocol dependencies
- Identify failure propagation paths
- Calculate amplification factors
- Design trigger sequences
- Assess containment barriers

#### System Corruption Techniques
- Identify state manipulation vectors
- Map persistence mechanisms
- Design corruption payloads
- Calculate recovery complexity
- Assess detection likelihood

#### Emergency Function Abuse
- Map all emergency mechanisms
- Identify privilege escalation paths
- Design bypass sequences
- Calculate extraction potential
- Assess response time

#### Governance Attack Chains
- Map governance processes
- Identify acceleration mechanisms
- Design proposal payloads
- Calculate voting requirements
- Assess execution delays

### 3. Advanced Attack Strategies

#### Attack Synchronization
- Multi-protocol coordination
- Cross-chain timing alignment
- MEV bundle construction
- Flash loan sequencing
- Oracle manipulation timing

#### Defense Evasion
- Anomaly detection bypasses
- Rate limit circumvention
- Circuit breaker defeats
- Monitoring blind spots
- Alert fatigue exploitation

#### Persistence Mechanisms
- Hidden backdoor installation
- State corruption anchoring
- Upgrade path hijacking
- Recovery prevention
- Long-term access maintenance

## Documentation Requirements

For each compound attack:
- **Attack Composition**: Individual vectors combined
- **Execution Timeline**: Detailed phase progression
- **Resource Requirements**: Capital, gas, timing needs
- **Success Probability**: Statistical analysis
- **Impact Assessment**: Total damage potential
- **Detection Difficulty**: Evasion techniques used
- **Recovery Complexity**: Post-attack remediation

## Validation Criteria
- Demonstrate realistic execution paths
- Calculate actual profit potential
- Consider defensive mechanisms
- Account for real-world constraints
- Provide mitigation strategies

## Special Focus Areas

### Multi-Vector Coordination
```solidity
// Compound vulnerability example:
// Step 1: Oracle Manipulation
function manipulateOracle() external {
    // Flash loan to manipulate price
    flashLoan.borrow(largeAmount);
    // Skew AMM reserves
    amm.swap(token0, token1, largeAmount);
    // Update oracle with manipulated price
    oracle.update();
}

// Step 2: Liquidation Attack (same transaction)
function exploitLiquidation() external {
    // Use manipulated price to trigger liquidations
    lending.liquidate(targetPositions);
    // Profit from discounted collateral
}

// Step 3: Governance Attack (next block)
function exploitGovernance() external {
    // Use profits to gain voting power
    govToken.delegate(attacker);
    // Submit malicious proposal
    governance.propose(maliciousUpgrade);
}
```

### Cascading Failure Design
```solidity
// Cascade trigger pattern:
contract CascadeAttack {
    // Phase 1: Initial vulnerability
    function triggerInitialFailure() external {
        // Exploit reentrancy in Protocol A
        protocolA.vulnerableWithdraw();
        // Causes imbalance in shared pool
    }
    
    // Phase 2: Propagation
    function propagateFailure() external {
        // Protocol B relies on Protocol A's state
        // Imbalance causes miscalculation
        protocolB.calculateRewards(); // Overflows
        
        // Protocol C uses Protocol B's output
        protocolC.updatePrices(); // Corrupted
    }
    
    // Phase 3: Amplification
    function amplifyDamage() external {
        // Corrupted prices trigger mass liquidations
        // Liquidations cause further price crashes
        // Death spiral across ecosystem
    }
}
```

### System Corruption Payload
```solidity
// Complete corruption attack:
contract SystemCorruption {
    // Corrupt global state
    function corruptState() external {
        // Exploit storage collision
        assembly {
            // Overwrite critical slots
            sstore(0x0, attacker)
            sstore(0x1, maliciousImpl)
            // Corrupt mapping structures
            mstore(0x0, targetMapping)
            mstore(0x20, key)
            let slot := keccak256(0x0, 0x40)
            sstore(slot, corruptedValue)
        }
    }
    
    // Install persistent backdoor
    function installBackdoor() external {
        // Hijack delegatecall
        implementation = backdoorContract;
        // Modify proxy admin
        admin = attacker;
        // Corrupt upgrade logic
        upgradeability.disable();
    }
}
```

### Emergency Drain Sequence
```solidity
// Emergency function chain:
contract EmergencyDrain {
    // Step 1: Trigger emergency
    function createEmergency() external {
        // Manipulate protocol metrics
        oracle.reportCriticalPrice();
        // Trigger automatic emergency
        protocol.enterEmergencyMode();
    }
    
    // Step 2: Exploit emergency powers
    function drainFunds() external {
        // Emergency mode allows withdrawals
        emergencyWithdraw(allFunds);
        // Bypass timelock in emergency
        timelock.executeImmediate(drain);
    }
}
```

### Phased Attack Implementation
```solidity
// Time-delayed multi-phase attack:
contract PhasedAttack {
    uint256 constant PHASE_DELAY = 30 days;
    uint256 public currentPhase;
    
    // Phase 0: Establish trust
    function phase0_buildReputation() external {
        // Provide liquidity
        // Participate in governance
        // Build protocol integration
    }
    
    // Phase 1: Plant vulnerabilities
    function phase1_prepareExploit() external {
        require(block.timestamp > deployTime + PHASE_DELAY);
        // Submit "improvement" proposals
        // Insert subtle vulnerabilities
        // Gain admin privileges
    }
    
    // Phase 2: Execute attack
    function phase2_exploit() external {
        require(block.timestamp > deployTime + PHASE_DELAY * 2);
        // Activate dormant vulnerabilities
        // Drain protocol funds
        // Corrupt state permanently
    }
}
```

### Randomized Attack Patterns
```solidity
// Non-deterministic attack selection:
contract RandomizedAttack {
    function executeRandomAttack(uint256 seed) external {
        uint256 random = uint256(keccak256(abi.encodePacked(block.timestamp, seed)));
        uint256 attackVector = random % 10;
        
        if (attackVector == 0) {
            executeReentrancyAttack();
        } else if (attackVector == 1) {
            executeOracleManipulation();
        } else if (attackVector == 2) {
            executeGovernanceTakeover();
        }
        // ... more attack options
        
        // Recursive random continuation
        if (random % 3 == 0) {
            executeRandomAttack(random);
        }
    }
}
```

### Complete Suite Deployment
```solidity
// All vectors simultaneous execution:
contract CompleteAttackSuite {
    function executeAllAttacks() external {
        // Deploy all attack contracts
        address[] memory attacks = deployAttackContracts();
        
        // Execute in parallel using multicall
        bytes[] memory calls = new bytes[](attacks.length);
        for (uint i = 0; i < attacks.length; i++) {
            calls[i] = abi.encodeWithSignature("attack()");
        }
        
        multicall.aggregate(attacks, calls);
        
        // Compound the damage
        combineAttackResults();
        
        // Extract maximum value
        drainAllProtocols();
    }
}
```

Focus on identifying compound vulnerabilities that when combined create catastrophic failure scenarios. Pay special attention to attack choreography, timing requirements, and the multiplicative effects of combining multiple attack vectors. Consider both technical and economic factors in designing comprehensive attack scenarios."""