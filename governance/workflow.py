"""Governance vulnerability detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="governance")
def factory():
    """Run governance attack vector detector."""
    return GovernanceDetector()


class GovernanceDetector(SimpleDetector):
    """Advanced governance vulnerability detector covering 8 major attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the governance vulnerability detection workflow."""
        return """# Governance Attack Vector Analysis

## Task
Perform comprehensive governance vulnerability analysis targeting 8 critical attack vectors from the VectorGuard Labs Attack Suite.

## Target Attack Vectors

### 🔴 Critical Severity
1. **Governance Function Attack** - Direct governance function exploitation
2. **Timelock Bypass** - Governance timelock circumvention 
3. **Enhanced Governance Attack with Flash Loans** - Flash loan + governance combination
4. **Compound Governance Attack** - Compound-specific governance exploits
5. **Aragon Voting Attack** - Aragon DAO voting manipulation
6. **DAOstack Proposal Attack** - DAOstack proposal exploitation

### 🟡 High Severity  
7. **Moloch Ragequit Attack** - Moloch DAO ragequit exploitation
8. **Snapshot Off-Chain Attack** - Off-chain voting manipulation

## Analysis Process

### 1. Discovery Phase
- Map governance architecture (contracts, roles, permissions)
- Identify voting mechanisms (on-chain, off-chain, hybrid)
- Locate timelock contracts and delay mechanisms
- Find proposal creation and execution functions
- Check for flash loan integration points

### 2. Attack Vector Analysis

#### Governance Function Attacks
- Search for unprotected admin functions (`onlyOwner`, `onlyGovernance`)
- Check access control bypass patterns
- Verify multi-sig requirements and threshold validations
- Look for role escalation vulnerabilities

#### Timelock Bypass Vulnerabilities  
- Analyze timelock delay enforcement
- Check for emergency execution backdoors
- Verify proposal queuing and execution flow
- Look for timestamp manipulation vulnerabilities

#### Flash Loan Integration Risks
- Identify governance tokens that can be flash borrowed
- Check voting power calculation timing
- Analyze snapshot mechanisms and block-based voting
- Look for same-block governance attacks

#### DAO Framework Specific Issues
- **Compound**: Check delegation, proposal thresholds, quorum manipulation  
- **Aragon**: Verify voting app permissions, forwarding vulnerabilities
- **DAOstack**: Analyze reputation systems, proposal boosting attacks
- **Moloch**: Check ragequit mechanics, dilution attacks

#### Off-Chain Governance Risks
- Verify signature validation in Snapshot-style systems
- Check for replay attacks in off-chain voting
- Analyze IPFS content integrity for proposals
- Look for meta-transaction vulnerabilities

### 3. Exploitation Validation
For each finding, verify:
- Economic feasibility of the attack
- Required governance token holdings
- Timing constraints and execution windows
- Potential impact and fund exposure

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector Category**: Which of the 8 vectors it represents
- **Economic Impact**: Estimated funds at risk
- **Attack Prerequisites**: Required conditions/resources
- **Step-by-step Exploit**: Concrete attack scenario
- **Proof of Concept**: Solidity code demonstrating the attack
- **Remediation Strategy**: Specific fixes and best practices

## Validation Criteria
- Confirm actual exploitability, not theoretical issues
- Verify economic incentives align with attack costs  
- Ensure attack scenarios account for real-world constraints
- Provide actionable remediation with code examples
- Classify severity based on funds at risk and likelihood

Focus on high-impact vulnerabilities that could lead to governance takeover, fund theft, or protocol disruption."""