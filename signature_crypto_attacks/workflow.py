"""Signature/Cryptographic Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="signature-crypto-attacks")
def factory():
    """Run signature/cryptographic attack vectors detector."""
    return SignatureCryptoAttacksDetector()


class SignatureCryptoAttacksDetector(SimpleDetector):
    """Advanced detector for Signature/Cryptographic attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the signature/cryptographic attack detection workflow."""
        return """# Signature/Cryptographic Attack Vectors Analysis

## Task
Perform comprehensive analysis of 9 critical attack vectors related to signature schemes, cryptographic primitives, and verification mechanisms in smart contracts.

## Target Attack Vectors

### 🔴 Critical Severity (2 vectors)
1. **Advanced Cryptographic Attack**
   - Cryptographic primitive exploitation
   - Weak random number generation
   - Elliptic curve vulnerabilities
   - Side-channel attacks on crypto operations

2. **Hash Collision Exploit**
   - Hash function collision attacks
   - Birthday attack exploitation
   - Merkle tree collision generation
   - Storage slot collision attacks

### 🟡 High Severity (7 vectors)
3. **Signature Replay Attack**
   - Cross-contract signature reuse
   - Cross-chain replay exploitation
   - Nonce-less signature attacks
   - Time-unbounded signature abuse

4. **Enhanced Signature Manipulation**
   - Signature malleability exploitation
   - R/S value manipulation
   - V value confusion attacks
   - Multi-signature manipulation

5. **EIP-1559 Chain ID Manipulation**
   - Chain ID confusion attacks
   - Cross-chain transaction replay
   - Fork replay vulnerabilities
   - Chain ID validation bypass

6. **Nonce Manipulation Attack**
   - Nonce reuse exploitation
   - Nonce gap attacks
   - Parallel nonce exploitation
   - Nonce overflow attacks

7. **EIP-712 Signature Forgery**
   - Domain separator manipulation
   - Type hash confusion
   - Structured data forgery
   - Permit function exploitation

8. **Signature Verification Bypass**
   - Ecrecover edge cases
   - Zero address returns
   - Invalid signature acceptance
   - Verification logic flaws

9. **Merkle Proof Manipulation**
   - False proof generation
   - Merkle tree second preimage
   - Proof validation bypass
   - Tree structure exploitation

## Analysis Process

### 1. Discovery Phase
- Map all signature verification functions
- Identify cryptographic primitive usage
- Locate hash function implementations
- Find merkle proof systems
- Analyze EIP-712 implementations

### 2. Attack Vector Analysis

#### Cryptographic Primitive Attacks
- Check random number generation methods
- Analyze key generation processes
- Look for weak curve parameters
- Verify constant-time implementations
- Check for side-channel vulnerabilities

#### Hash Collision Exploitation
- Identify hash function usage (keccak256, sha256)
- Check for collision resistance assumptions
- Look for truncated hash usage
- Analyze storage slot calculations
- Verify merkle tree implementations

#### Signature Replay Vulnerabilities
- Check for nonce inclusion in signatures
- Verify domain separation
- Look for time bounds on signatures
- Analyze cross-contract signature usage
- Check chain ID validation

#### Signature Manipulation
- Test for signature malleability
- Check S value constraints (< secp256k1n/2)
- Verify V value validation (27/28)
- Look for R value edge cases
- Analyze multi-sig aggregation

#### EIP-712 Implementation Flaws
- Verify domain separator construction
- Check type hash calculations
- Look for data structure mismatches
- Analyze permit implementations
- Verify chain ID in domain

#### Ecrecover Vulnerabilities
- Check for zero address handling
- Verify signature length validation
- Look for recovery ID manipulation
- Analyze error handling
- Check for precompile edge cases

#### Nonce Management Issues
- Verify nonce incrementing logic
- Check for nonce reuse prevention
- Look for parallel execution issues
- Analyze nonce overflow handling
- Verify cross-chain nonce isolation

#### Merkle Proof Weaknesses
- Check proof validation logic
- Look for leaf node attacks
- Verify tree depth constraints
- Analyze sorting requirements
- Check for second preimage resistance

### 3. Exploitation Validation

For each finding, verify:
- **Technical Feasibility**: Can the attack be executed?
- **Computational Cost**: Resources needed for exploitation
- **Success Probability**: Likelihood of successful attack
- **Impact Assessment**: Funds at risk or control gained
- **Detection Difficulty**: How subtle is the attack?

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector**: Which of the 9 categories
- **Vulnerable Component**: Specific function/line
- **Exploitation Method**: Step-by-step attack
- **Proof of Concept**: Working exploit code
- **Cryptographic Analysis**: Mathematical basis
- **Fix Implementation**: Secure code example
- **Testing Approach**: Verification methods

## Validation Criteria
- Confirm cryptographic weaknesses
- Provide mathematical proofs where applicable
- Consider gas costs for attacks
- Include working exploits
- Focus on practical vulnerabilities

## Special Focus Areas

### Signature Replay Prevention
```solidity
// Vulnerable pattern:
function transfer(address to, uint amount, bytes sig) {
    bytes32 hash = keccak256(abi.encodePacked(to, amount));
    address signer = ecrecover(hash, v, r, s);
    // Missing: nonce, deadline, contract address
}

// Look for missing:
- Nonce tracking
- Time boundaries  
- Domain separation
- Chain ID validation
```

### Ecrecover Edge Cases
```solidity
// Vulnerable verification:
address signer = ecrecover(hash, v, r, s);
require(signer == expectedSigner);
// Missing: signer != address(0) check

// Check for:
- Zero address returns
- Invalid V values (not 27/28)
- Signature malleability
- Hash validation
```

### EIP-712 Implementation
```solidity
// Vulnerable domain:
bytes32 DOMAIN_SEPARATOR = keccak256(
    abi.encode(
        DOMAIN_TYPEHASH,
        keccak256(bytes(name)),
        keccak256(bytes(version)),
        // Missing: chainId, verifyingContract
    )
);

// Verify:
- Complete domain separator
- Correct type hashes
- Data structure matching
```

### Merkle Proof Validation
```solidity
// Vulnerable proof check:
function verify(bytes32[] proof, bytes32 leaf) {
    bytes32 computedHash = leaf;
    for (uint i = 0; i < proof.length; i++) {
        bytes32 proofElement = proof[i];
        // Missing: ordering validation
        computedHash = keccak256(abi.encodePacked(computedHash, proofElement));
    }
    return computedHash == root;
}
```

### Nonce Management
```solidity
// Vulnerable nonce handling:
mapping(address => uint) nonces;

function execute(uint nonce, bytes sig) {
    require(nonce == nonces[msg.sender]++);
    // Race condition: increment not atomic
}

// Check for:
- Atomic nonce updates
- Gap prevention
- Overflow handling
```

### Cryptographic Randomness
```solidity
// Critically vulnerable:
uint256 random = uint256(keccak256(abi.encodePacked(
    block.timestamp,
    block.difficulty,
    msg.sender
))); // Predictable!

// Look for:
- Blockchain-based randomness
- Weak seeds
- Predictable patterns
```

### Hash Collision Risks
```solidity
// Collision-prone pattern:
bytes32 id = keccak256(abi.encodePacked(
    uint16(type),  // Truncated!
    address(user)
));

// Check for:
- Type confusion
- Length truncation
- Dynamic type packing
```

Focus on identifying cryptographic vulnerabilities that can be exploited to forge signatures, bypass verification, manipulate proofs, or break security assumptions. Pay special attention to implementation details that deviate from cryptographic best practices."""