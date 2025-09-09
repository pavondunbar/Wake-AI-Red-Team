"""Identity/Naming Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="identity-naming-attacks")
def factory():
    """Run identity/naming attack vectors detector."""
    return IdentityNamingAttacksDetector()


class IdentityNamingAttacksDetector(SimpleDetector):
    """Advanced detector for Identity and Naming System attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the identity/naming attack detection workflow."""
        return """# Identity/Naming Attack Vectors Analysis

## Task
Perform comprehensive analysis of 5 attack vectors targeting decentralized identity and naming systems including ENS, Unstoppable Domains, BrightID, Civic Identity, and Proof of Humanity, focusing on identity spoofing, domain hijacking, and verification bypasses.

## Target Attack Vectors

### 🟡 High Severity (2 vectors)
1. **ENS Attack**
   - Domain hijacking and squatting
   - Resolver manipulation attacks
   - Subdomain takeover exploits
   - Reverse resolution spoofing
   - Registrar controller exploitation

2. **Unstoppable Domains Attack**
   - Domain resolution manipulation
   - Metadata spoofing attacks
   - Registry controller exploitation
   - Cross-chain domain conflicts
   - IPFS content hijacking

### 🟠 Medium Severity (3 vectors)
3. **BrightID Attack**
   - Identity graph manipulation
   - Sybil attack coordination
   - Verification node compromise
   - Connection spoofing
   - Uniqueness proof bypasses

4. **Civic Identity Attack**
   - Identity verification bypasses
   - Credential spoofing attacks
   - Verifier node manipulation
   - Biometric data exploitation
   - KYC process gaming

5. **Proof of Humanity Attack**
   - Submission process gaming
   - Challenge system exploitation
   - Evidence manipulation
   - Vouching system abuse
   - Identity farming attacks

## Analysis Process

### 1. Discovery Phase
- Map identity system architectures
- Identify verification mechanisms
- Locate resolver systems
- Find registration processes
- Analyze trust assumptions

### 2. Attack Vector Analysis

#### Domain System Attacks
- Check domain registration logic
- Analyze resolver implementations
- Look for subdomain vulnerabilities
- Test reverse resolution accuracy
- Verify controller permissions

#### Identity Verification Bypasses
- Map verification workflows
- Check credential validation
- Look for proof bypasses
- Test uniqueness mechanisms
- Verify challenge systems

#### Reputation System Gaming
- Check vouching mechanisms
- Analyze trust propagation
- Look for circular vouching
- Test reputation accumulation
- Verify penalty systems

#### Cross-System Identity Conflicts
- Check identity portability
- Analyze cross-platform verification
- Look for namespace collisions
- Test identity synchronization
- Verify uniqueness across systems

### 3. Identity-Specific Exploit Patterns

#### Domain Hijacking Techniques
- Expired domain takeovers
- DNS poisoning attacks
- Resolver manipulation
- Subdomain enumeration
- Registrar vulnerabilities

#### Identity Spoofing Methods
- Biometric bypasses
- Credential forgery
- Social engineering
- Document manipulation
- Verification gaming

#### Sybil Attack Coordination
- Multiple identity creation
- Reputation washing
- Collusive vouching
- Identity farming
- Verification bypasses

## Documentation Requirements

For each identity attack:
- **System Affected**: Specific identity/naming platform
- **Attack Category**: Domain, verification, or reputation
- **Identity Requirements**: What identities are needed
- **Social Engineering**: Human interaction requirements
- **Technical Exploitation**: Smart contract vulnerabilities
- **Detection Difficulty**: How hidden the attack is
- **Impact Assessment**: Reputation and trust damage

## Validation Criteria
- Test with realistic identity scenarios
- Consider social engineering factors
- Verify technical feasibility
- Account for verification delays
- Provide identity-aware defenses

## Special Focus Areas

### ENS Domain Hijacking
```solidity
// ENS domain takeover attack:
contract ENSAttack {
    IENS public ens;
    IENSRegistrar public registrar;
    IResolver public resolver;
    
    function hijackExpiredDomain(string memory domain) external {
        bytes32 node = namehash(domain);
        
        // Step 1: Check if domain expired
        require(registrar.available(domain), "Domain not expired");
        
        // Step 2: Register expired domain
        uint256 duration = 365 days;
        registrar.register(domain, address(this), duration);
        
        // Step 3: Set malicious resolver
        ens.setResolver(node, address(maliciousResolver));
        
        // Step 4: Point domain to attacker's address
        resolver.setAddr(node, attackerAddress);
        
        // Users sending to ENS domain now send to attacker
    }
    
    function subdomainTakeover(string memory domain, string memory subdomain) external {
        bytes32 parentNode = namehash(domain);
        bytes32 subNode = namehash(string(abi.encodePacked(subdomain, ".", domain)));
        
        // Step 1: Check if subdomain owner is zero address
        address subdomainOwner = ens.owner(subNode);
        require(subdomainOwner == address(0), "Subdomain already owned");
        
        // Step 2: If we own parent, set subdomain
        require(ens.owner(parentNode) == address(this), "Don't own parent domain");
        
        // Step 3: Set subdomain to attacker
        ens.setSubnodeOwner(parentNode, keccak256(bytes(subdomain)), attackerAddress);
        
        // Step 4: Set malicious resolver for subdomain
        ens.setResolver(subNode, address(maliciousResolver));
    }
    
    function resolverManipulation(bytes32 node) external {
        // If we control resolver, we can manipulate all resolutions
        require(ens.resolver(node) == address(this), "Not the resolver");
        
        // Return attacker address for any addr() call
        // This affects all applications using this resolver
    }
    
    function reverseResolutionSpoofing() external {
        // Step 1: Set reverse record to point to target domain
        bytes32 reverseNode = getReverseNode(address(this));
        ens.setResolver(reverseNode, address(this));
        
        // Step 2: When applications do reverse lookup, return fake name
        INameResolver(address(this)).name(reverseNode); // Returns spoofed name
    }
}
```

### Unstoppable Domains Exploitation
```solidity
// Unstoppable Domains attack:
contract UnstoppableAttack {
    IRegistry public registry;
    IResolver public resolver;
    
    function hijackUnstoppableDomain(string memory domain) external {
        uint256 tokenId = uint256(keccak256(bytes(domain)));
        
        // Step 1: Check if domain is available or expired
        try registry.ownerOf(tokenId) returns (address owner) {
            require(owner == address(0), "Domain owned");
        } catch {
            // Domain available
        }
        
        // Step 2: Register domain through registry
        registry.mintDomain(address(this), domain);
        
        // Step 3: Set malicious records
        string[] memory keys = new string[](3);
        string[] memory values = new string[](3);
        
        keys[0] = "crypto.ETH.address";
        values[0] = addressToString(attackerAddress);
        
        keys[1] = "ipfs.html.value";
        values[1] = maliciousIPFSHash;
        
        keys[2] = "dns.A";
        values[2] = maliciousIPAddress;
        
        resolver.setMany(keys, values, tokenId);
    }
    
    function metadataSpoofing(uint256 tokenId) external {
        // If we control domain, manipulate metadata
        require(registry.ownerOf(tokenId) == address(this), "Not owner");
        
        // Set misleading metadata
        registry.set("social.twitter.username", "legitimate_account", tokenId);
        registry.set("validation.social.twitter", "verified", tokenId);
        
        // Users think this is verified legitimate account
    }
    
    function crossChainConflicts(string memory domain) external {
        // Register same domain on different chains with different owners
        // Chain A: legitimate owner
        // Chain B: attacker registers same domain
        
        uint256 tokenId = uint256(keccak256(bytes(domain)));
        registry.mintDomain(address(this), domain);
        
        // Now applications using Chain B resolver get attacker's address
        // While Chain A has legitimate owner
    }
}
```

### BrightID Sybil Attack
```solidity
// BrightID identity graph manipulation:
contract BrightIDAttack {
    IBrightID public brightID;
    
    function createSybilNetwork() external {
        // Step 1: Create multiple fake identities
        address[] memory sybilAddresses = new address[](50);
        
        for (uint i = 0; i < 50; i++) {
            sybilAddresses[i] = createFakeIdentity();
        }
        
        // Step 2: Connect sybil identities to each other
        createSybilConnections(sybilAddresses);
        
        // Step 3: Connect some sybils to legitimate users
        connectToLegitimateUsers(sybilAddresses);
        
        // Step 4: Use sybil network for verification gaming
        gameBrightIDVerification();
    }
    
    function manipulateVerificationNodes() external {
        // Step 1: Identify verification node operators
        address[] memory verifiers = getVerificationNodes();
        
        // Step 2: Social engineer or bribe verifiers
        for (uint i = 0; i < verifiers.length; i++) {
            attemptVerifierCompromise(verifiers[i]);
        }
        
        // Step 3: Use compromised verifiers to approve fake identities
        approveFakeIdentities();
    }
    
    function connectionSpoofing() external {
        // Create fake connections to boost reputation
        
        // Step 1: Identify high-reputation users
        address[] memory targetUsers = findHighReputationUsers();
        
        // Step 2: Create connection claims
        for (uint i = 0; i < targetUsers.length; i++) {
            claimConnection(targetUsers[i]);
        }
        
        // Step 3: If connections not verified properly, gain reputation
        boostReputationThroughFakeConnections();
    }
}
```

### Civic Identity Verification Bypass
```solidity
// Civic identity system attack:
contract CivicAttack {
    ICivic public civic;
    
    function bypassKYCVerification() external {
        // Step 1: Create fake identity documents
        bytes memory fakeDocuments = createFakeDocuments();
        
        // Step 2: Submit for verification
        uint256 verificationId = civic.submitVerification(
            fakeDocuments,
            "John Doe",
            "1990-01-01",
            "US"
        );
        
        // Step 3: If automated verification, exploit weaknesses
        exploitAutomatedVerification(verificationId);
        
        // Step 4: If human verification, social engineer
        socialEngineerHumanVerifier(verificationId);
    }
    
    function exploitVerifierNodes() external {
        // Step 1: Identify verifier node operators
        address[] memory verifiers = civic.getVerifiers();
        
        // Step 2: Target least secure verifiers
        address targetVerifier = findWeakestVerifier(verifiers);
        
        // Step 3: Compromise verifier infrastructure
        compromiseVerifierNode(targetVerifier);
        
        // Step 4: Approve fake identities through compromised node
        approveFakeVerifications();
    }
    
    function biometricSpoofing() external {
        // Attack biometric verification systems
        
        // Step 1: Obtain target's biometric data
        bytes memory stolenBiometrics = obtainStolenBiometrics();
        
        // Step 2: Create synthetic biometrics
        bytes memory syntheticBiometrics = createSyntheticBiometrics(stolenBiometrics);
        
        // Step 3: Submit for verification
        civic.submitBiometricVerification(syntheticBiometrics);
        
        // If successful, gain verified identity of target
    }
}
```

### Proof of Humanity Gaming
```solidity
// Proof of Humanity submission gaming:
contract ProofOfHumanityAttack {
    IProofOfHumanity public poh;
    
    function gameSubmissionProcess() external {
        // Step 1: Create fake identity evidence
        string memory fakeVideo = uploadFakeVideo();
        string memory fakePhoto = uploadFakePhoto();
        string memory fakeName = "John Doe";
        
        // Step 2: Submit fake human proof
        poh.addSubmission(
            fakeName,
            fakeVideo,
            fakePhoto
        );
        
        // Step 3: Coordinate vouching from controlled accounts
        coordinateVouching();
        
        // Step 4: Challenge legitimate challengers
        challengeLegitimateChallengers();
    }
    
    function exploitChallengeSystem() external {
        // Step 1: Identify submissions near expiry
        address[] memory submissions = findNearExpirySubmissions();
        
        // Step 2: Submit frivolous challenges to waste challenger deposits
        for (uint i = 0; i < submissions.length; i++) {
            submitFrivolousChallenge(submissions[i]);
        }
        
        // Step 3: If challenge fails, collect challenger deposits
        collectFailedChallengeDeposits();
    }
    
    function vouchingSystemAbuse() external {
        // Step 1: Create network of verified accounts
        address[] memory controlledAccounts = createVerifiedAccountNetwork();
        
        // Step 2: Use accounts to vouch for fake submissions
        for (uint i = 0; i < controlledAccounts.length; i++) {
            poh.addVouch(controlledAccounts[i], fakeSubmissionAddress);
        }
        
        // Step 3: Create circular vouching patterns
        createCircularVouching(controlledAccounts);
    }
    
    function identityFarming() external {
        // Large scale identity creation
        
        // Step 1: Create multiple fake identities
        for (uint i = 0; i < 100; i++) {
            address fakeIdentity = createFakeIdentity();
            submitFakeHumanProof(fakeIdentity);
        }
        
        // Step 2: Use identities for various attacks
        // - Governance manipulation
        // - Airdrop farming  
        // - Platform abuse
        
        exploitVerifiedIdentities();
    }
}
```

### Cross-Platform Identity Conflicts
```solidity
// Multi-platform identity attack:
contract CrossPlatformAttack {
    mapping(string => address) public platforms;
    
    function exploitIdentityConflicts() external {
        string memory targetIdentity = "john.doe";
        
        // Step 1: Register identity on multiple platforms with different owners
        registerOnENS(targetIdentity, attackerAddress1);
        registerOnUnstoppable(targetIdentity, attackerAddress2);
        registerOnBrightID(targetIdentity, attackerAddress3);
        
        // Step 2: Applications using different platforms get different results
        // This creates confusion and potential for exploitation
        
        // Step 3: Social engineer users to use platform we control
        manipulateUserChoice();
    }
    
    function namespaceCollision() external {
        // Exploit namespace collisions across platforms
        
        string[] memory popularNames = getPopularNames();
        
        for (uint i = 0; i < popularNames.length; i++) {
            // Register on all platforms we don't control yet
            registerAcrossPlatforms(popularNames[i]);
        }
        
        // Users confused about which platform/owner is legitimate
    }
    
    function reputationWashing() external {
        // Transfer reputation across platforms
        
        // Step 1: Build reputation on one platform
        buildReputationOnPlatformA();
        
        // Step 2: Claim same identity on other platforms
        claimIdentityOnPlatformB();
        claimIdentityOnPlatformC();
        
        // Step 3: Use cross-platform reputation for attacks
        exploitCrossReputationTrust();
    }
}
```

### Domain Squatting and Phishing
```solidity
// Domain squatting for phishing:
contract DomainSquattingAttack {
    function registerPhishingDomains() external {
        // Register domains similar to popular services
        string[] memory phishingDomains = [
            "uniswap.crypto",    // vs uniswap.org
            "opensea.nft",       // vs opensea.io  
            "metamask.wallet",   // vs metamask.io
            "coinbase.exchange", // vs coinbase.com
            "binance.trade"      // vs binance.com
        ];
        
        for (uint i = 0; i < phishingDomains.length; i++) {
            registerDomain(phishingDomains[i]);
            setPhishingContent(phishingDomains[i]);
        }
    }
    
    function typosquattingAttack() external {
        // Register typosquatted versions
        string[] memory typos = [
            "uniswap.crypto",  // legitimate
            "uniswp.crypto",   // missing 'a'
            "uniswap.cryto",   // missing 'p' 
            "uniswaap.crypto", // double 'a'
            "uniswap.crypt"    // missing 'o'
        ];
        
        registerPhishingVariants(typos);
    }
    
    function homographAttack() external {
        // Use unicode characters that look similar
        registerDomain("uniswαp.crypto"); // Greek alpha instead of 'a'
        registerDomain("unіswap.crypto"); // Cyrillic 'і' instead of 'i'
        registerDomain("uniswap.сrypto"); // Cyrillic 'с' instead of 'c'
        
        // Visually identical but different domains
        setupHomographPhishing();
    }
}
```

Focus on identifying vulnerabilities in decentralized identity and naming systems, including domain hijacking, identity spoofing, verification bypasses, and reputation system gaming. Pay special attention to the social engineering aspects and cross-platform identity conflicts that can arise in decentralized identity ecosystems."""