"""NFT Attack Vectors detector for Wake-AI framework."""

from wake_ai import workflow
from wake_ai.templates import SimpleDetector


@workflow.command(name="nft-attacks")
def factory():
    """Run NFT attack vectors detector."""
    return NFTAttacksDetector()


class NFTAttacksDetector(SimpleDetector):
    """Advanced detector covering 4 NFT attack vectors from VectorGuard Labs."""

    def get_detector_prompt(self) -> str:
        """Define the NFT attack vectors detection workflow."""
        return """# NFT Attack Vectors Analysis

## Task
Perform comprehensive analysis of 4 critical NFT (Non-Fungible Token) vulnerabilities that exploit marketplace mechanisms, royalty systems, and batch operations in NFT ecosystems.

## Target Attack Vectors

### 🟡 High Severity (4 vectors)
1. **ERC1155 Batch Attack** - ERC1155 batch operation exploitation
2. **NFT Royalty Bypass Attack** - Royalty circumvention
3. **OpenSea Wyvern Attack** - OpenSea marketplace exploitation
4. **Rarible Royalty Attack** - Rarible royalty bypass

## Analysis Process

### 1. Discovery Phase
- Map NFT contract implementations (ERC721, ERC1155)
- Identify marketplace integrations (OpenSea, Rarible, LooksRare)
- Locate royalty enforcement mechanisms and standards
- Find batch operation functions and access controls
- Analyze metadata and URI handling systems

### 2. Attack Vector Analysis

#### ERC1155 Batch Operation Exploitation
```solidity
// ERC1155 batch attack patterns:
contract ERC1155BatchAttack {
    IERC1155 public nftContract;
    
    function batchAttack() external {
        // ERC1155-specific vulnerabilities:
        
        // 1. Batch operation reentrancy
        // - Reentrancy during batch transfers
        // - State inconsistency in batch operations
        // - Gas manipulation in batch calls
        
        // 2. Batch approval exploitation
        // - setApprovalForAll manipulation
        // - Batch transfer without proper checks
        // - Cross-contract batch interactions
        
        // 3. Balance manipulation attacks
        // - Batch mint/burn inconsistencies
        // - Supply tracking errors in batches
        // - Metadata corruption via batch ops
        
        executeBatchExploit();
    }
    
    function reentrancyBatchAttack(
        address to,
        uint256[] memory ids,
        uint256[] memory amounts,
        bytes memory data
    ) external {
        // Vulnerable batch transfer with reentrancy
        nftContract.safeBatchTransferFrom(address(this), to, ids, amounts, data);
    }
    
    function onERC1155BatchReceived(
        address operator,
        address from,
        uint256[] memory ids,
        uint256[] memory values,
        bytes memory data
    ) external returns (bytes4) {
        // Reentrancy point during batch transfer
        if (reentryCount < MAX_REENTRY) {
            reentryCount++;
            // Manipulate state during callback
            manipulateContractState();
            
            // Continue reentrancy
            nftContract.safeBatchTransferFrom(
                address(this),
                targetAddress,
                newIds,
                newAmounts,
                ""
            );
        }
        
        return this.onERC1155BatchReceived.selector;
    }
}
```

#### NFT Royalty Bypass Attacks
```solidity
// Generic royalty bypass techniques:
contract RoyaltyBypassAttack {
    IERC721 public nftContract;
    IERC2981 public royaltyContract;
    
    function royaltyBypass() external {
        // Common royalty bypass methods:
        
        // 1. Direct transfer bypass
        // - Use transferFrom instead of marketplace
        // - Bypass marketplace royalty enforcement
        // - Off-chain transaction coordination
        
        // 2. Wrapper contract bypass
        // - Wrap NFT in custom contract
        // - Trade wrapper tokens without royalties
        // - Unwrap after trade completion
        
        // 3. Marketplace shopping
        // - Use marketplaces without royalty enforcement
        // - Exploit inconsistent royalty implementations
        // - Cross-marketplace arbitrage without royalties
        
        executeRoyaltyBypass();
    }
    
    function directTransferBypass(uint256 tokenId, address newOwner) external {
        // Bypass marketplace royalties with direct transfer
        require(nftContract.ownerOf(tokenId) == msg.sender, "Not owner");
        
        // Direct transfer - no royalties paid
        nftContract.transferFrom(msg.sender, newOwner, tokenId);
        
        // Off-chain payment coordination (bypasses royalties)
        // Payment handled outside of blockchain
    }
    
    function wrapperBypass(uint256 tokenId) external {
        // Step 1: Wrap NFT
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        wrapperToken.mint(msg.sender, tokenId);
        
        // Step 2: Trade wrapper token (no royalties on wrapper)
        // Marketplace trades happen on wrapper contract
        
        // Step 3: Unwrap after trade
        // New owner unwraps to get original NFT
        // Original royalties bypassed
    }
}
```

#### OpenSea Wyvern Protocol Exploitation
```solidity
// OpenSea Wyvern-specific attacks:
contract WyvernAttack {
    IWyvernExchange public wyvernExchange;
    
    function wyvernAttack() external {
        // Wyvern protocol vulnerabilities:
        
        // 1. Order manipulation
        // - Exploit order matching logic
        // - Signature replay attacks
        // - Order cancellation front-running
        
        // 2. Proxy registry exploitation
        // - Proxy contract manipulation
        // - Unauthorized proxy calls
        // - Registry poisoning attacks
        
        // 3. Fee manipulation
        // - Exploit fee calculation
        // - Platform fee bypass
        // - Maker/taker fee manipulation
        
        // 4. Metadata manipulation
        // - Asset contract spoofing
        // - Token ID manipulation
        // - Collection verification bypass
        
        executeWyvernExploit();
    }
    
    function orderManipulationAttack(
        Order memory buyOrder,
        Order memory sellOrder,
        bytes memory buySignature,
        bytes memory sellSignature
    ) external {
        // Manipulate order parameters before matching
        // Exploit order validation weaknesses
        
        // Front-run order cancellation
        if (canFrontRunCancellation(buyOrder)) {
            wyvernExchange.atomicMatch_(
                [buyOrder.exchange, buyOrder.maker, buyOrder.taker, buyOrder.feeRecipient, buyOrder.target, buyOrder.staticTarget, buyOrder.paymentToken],
                [buyOrder.makerRelayerFee, buyOrder.takerRelayerFee, buyOrder.makerProtocolFee, buyOrder.takerProtocolFee, buyOrder.basePrice, buyOrder.extra, buyOrder.listingTime, buyOrder.expirationTime, buyOrder.salt],
                [buyOrder.feeMethod, buyOrder.side, buyOrder.saleKind, buyOrder.howToCall],
                buyOrder.calldata,
                buyOrder.replacementPattern,
                buyOrder.staticExtradata,
                buySignature,
                [sellOrder.exchange, sellOrder.maker, sellOrder.taker, sellOrder.feeRecipient, sellOrder.target, sellOrder.staticTarget, sellOrder.paymentToken],
                [sellOrder.makerRelayerFee, sellOrder.takerRelayerFee, sellOrder.makerProtocolFee, sellOrder.takerProtocolFee, sellOrder.basePrice, sellOrder.extra, sellOrder.listingTime, sellOrder.expirationTime, sellOrder.salt],
                [sellOrder.feeMethod, sellOrder.side, sellOrder.saleKind, sellOrder.howToCall],
                sellOrder.calldata,
                sellOrder.replacementPattern,
                sellOrder.staticExtradata,
                sellSignature
            );
        }
    }
    
    function proxyRegistryAttack(address target, bytes memory callData) external {
        // Exploit proxy registry to make unauthorized calls
        IProxyRegistry proxyRegistry = wyvernExchange.registry();
        
        // Check if we can manipulate proxy
        if (canManipulateProxy(target)) {
            // Make unauthorized call through proxy
            address proxy = proxyRegistry.proxies(target);
            IProxy(proxy).proxy(target, callData);
        }
    }
}
```

#### Rarible Royalty System Exploitation
```solidity
// Rarible-specific royalty bypass:
contract RaribleRoyaltyAttack {
    IRaribleExchange public raribleExchange;
    IERC2981 public royaltyRegistry;
    
    function raribleRoyaltyAttack() external {
        // Rarible-specific vulnerabilities:
        
        // 1. Royalty registry manipulation
        // - Exploit royalty setting mechanisms
        // - Registry update front-running
        // - False royalty information
        
        // 2. Exchange contract bypass
        // - Use alternative transfer methods
        // - Exploit exchange logic flaws
        // - Custom asset contract exploitation
        
        // 3. Fee calculation manipulation
        // - Exploit royalty calculation bugs
        // - Rounding error exploitation
        // - Multiple royalty recipient confusion
        
        executeRaribleExploit();
    }
    
    function registryManipulationAttack(address nftContract, uint256 tokenId) external {
        // Attempt to manipulate royalty registry
        
        // Check if we can set royalties
        if (canSetRoyalties(nftContract)) {
            // Set royalties to zero or to attacker's address
            setRoyaltiesForContract(nftContract, 0, address(0));
        }
        
        // Exploit timing between registry update and trade
        frontRunRoyaltyUpdate(nftContract, tokenId);
    }
    
    function exchangeBypassAttack(
        address nftContract,
        uint256 tokenId,
        uint256 price
    ) external {
        // Bypass Rarible exchange to avoid royalties
        
        // Use direct contract interaction
        IERC721(nftContract).transferFrom(
            currentOwner,
            newOwner,
            tokenId
        );
        
        // Handle payment off-chain or through different contract
        // Royalties not enforced in direct transfer
    }
}
```

### 3. NFT Security Patterns Analysis

#### ERC1155 Security Issues
```solidity
// Vulnerable ERC1155 implementation:
contract VulnerableERC1155 {
    mapping(uint256 => mapping(address => uint256)) private _balances;
    mapping(address => mapping(address => bool)) private _operatorApprovals;
    
    function safeBatchTransferFrom(
        address from,
        address to,
        uint256[] memory ids,
        uint256[] memory amounts,
        bytes memory data
    ) public {
        // Vulnerable: no reentrancy protection
        for (uint256 i = 0; i < ids.length; ++i) {
            _balances[ids[i]][from] -= amounts[i];
            _balances[ids[i]][to] += amounts[i];
        }
        
        // Vulnerable: callback after state changes
        if (to.isContract()) {
            IERC1155Receiver(to).onERC1155BatchReceived(
                msg.sender, from, ids, amounts, data
            );
        }
    }
}
```

#### Royalty Enforcement Weaknesses
```solidity
// Weak royalty implementation:
contract WeakRoyalty {
    mapping(uint256 => RoyaltyInfo) public royalties;
    
    struct RoyaltyInfo {
        address recipient;
        uint256 percentage;
    }
    
    function transferWithRoyalty(
        uint256 tokenId,
        address from,
        address to,
        uint256 salePrice
    ) external {
        // Vulnerable: royalty payment not enforced
        RoyaltyInfo memory royalty = royalties[tokenId];
        uint256 royaltyAmount = salePrice * royalty.percentage / 10000;
        
        // Payment suggestion only - not enforced
        // require(msg.value >= royaltyAmount, "Insufficient royalty");
        
        _transfer(from, to, tokenId);
    }
}
```

### 4. Marketplace Integration Vulnerabilities

#### Cross-Marketplace Arbitrage
```solidity
// Cross-marketplace royalty arbitrage:
function crossMarketplaceArbitrage(
    uint256 tokenId,
    address lowRoyaltyMarketplace,
    address highPriceMarketplace
) external {
    // Buy from marketplace with poor royalty enforcement
    purchaseFromMarketplace(lowRoyaltyMarketplace, tokenId, lowPrice);
    
    // Sell on marketplace with higher prices
    sellOnMarketplace(highPriceMarketplace, tokenId, highPrice);
    
    // Profit from price difference minus avoided royalties
}
```

#### Metadata Manipulation
```solidity
// NFT metadata manipulation:
contract MetadataAttack {
    function manipulateMetadata(uint256 tokenId, string memory newURI) external {
        // Exploit mutable metadata
        if (canUpdateMetadata(tokenId)) {
            // Change metadata to more valuable asset
            updateTokenURI(tokenId, newURI);
            
            // List at higher price based on new metadata
            listForSale(tokenId, inflatedPrice);
        }
    }
}
```

### 5. Exploitation Validation
For each finding, verify:
- NFT standard compliance and implementation gaps
- Marketplace integration vulnerabilities
- Royalty enforcement mechanism weaknesses
- Batch operation security flaws
- Cross-platform compatibility issues

## Documentation Requirements

For each detected vulnerability:
- **Attack Vector Category**: Which of the 4 NFT vectors
- **NFT Standard Impact**: ERC721, ERC1155, or marketplace-specific
- **Royalty Bypass Method**: Specific technique used to avoid royalties
- **Marketplace Exploitation**: Platform-specific vulnerabilities
- **Economic Impact**: Estimated royalty losses or financial damage
- **Proof of Concept**: NFT-specific attack demonstration
- **Remediation Strategy**: Enhanced royalty enforcement, security improvements

## Validation Criteria
- Confirm NFT standard implementation vulnerabilities
- Verify royalty bypass techniques effectiveness
- Ensure marketplace-specific attack feasibility
- Provide concrete examples with popular NFT platforms
- Focus on vulnerabilities affecting creators and platform revenue

## Critical Security Patterns

### Secure ERC1155 Implementation
```solidity
// Secure ERC1155 with reentrancy protection:
contract SecureERC1155 {
    using ReentrancyGuard for bool;
    bool private _reentrancyGuard;
    
    function safeBatchTransferFrom(
        address from,
        address to,
        uint256[] memory ids,
        uint256[] memory amounts,
        bytes memory data
    ) public nonReentrant {
        require(
            from == msg.sender || isApprovedForAll(from, msg.sender),
            "ERC1155: caller is not owner nor approved"
        );
        
        _safeBatchTransferFrom(from, to, ids, amounts, data);
    }
    
    function _safeBatchTransferFrom(
        address from,
        address to,
        uint256[] memory ids,
        uint256[] memory amounts,
        bytes memory data
    ) internal {
        require(ids.length == amounts.length, "ERC1155: ids and amounts length mismatch");
        require(to != address(0), "ERC1155: transfer to the zero address");
        
        address operator = msg.sender;
        
        for (uint256 i = 0; i < ids.length; ++i) {
            uint256 id = ids[i];
            uint256 amount = amounts[i];
            
            uint256 fromBalance = _balances[id][from];
            require(fromBalance >= amount, "ERC1155: insufficient balance for transfer");
            unchecked {
                _balances[id][from] = fromBalance - amount;
            }
            _balances[id][to] += amount;
        }
        
        emit TransferBatch(operator, from, to, ids, amounts);
        
        _afterTokenTransfer(operator, from, to, ids, amounts, data);
        
        _doSafeBatchTransferAcceptanceCheck(operator, from, to, ids, amounts, data);
    }
}
```

### Enforced Royalty System
```solidity
// Mandatory royalty enforcement:
contract EnforcedRoyalty {
    IERC2981 public royaltyStandard;
    mapping(address => bool) public approvedMarketplaces;
    
    function transferWithEnforcedRoyalty(
        address nftContract,
        uint256 tokenId,
        address from,
        address to,
        uint256 salePrice
    ) external payable {
        require(approvedMarketplaces[msg.sender], "Unauthorized marketplace");
        
        // Calculate and enforce royalty payment
        (address royaltyRecipient, uint256 royaltyAmount) = 
            IERC2981(nftContract).royaltyInfo(tokenId, salePrice);
        
        require(msg.value >= royaltyAmount, "Insufficient royalty payment");
        
        // Transfer royalty
        if (royaltyAmount > 0) {
            payable(royaltyRecipient).transfer(royaltyAmount);
        }
        
        // Transfer remaining payment to seller
        payable(from).transfer(msg.value - royaltyAmount);
        
        // Transfer NFT
        IERC721(nftContract).transferFrom(from, to, tokenId);
    }
}
```

### Marketplace Security Framework
```solidity
// Secure marketplace integration:
contract SecureNFTMarketplace {
    mapping(address => bool) public verifiedContracts;
    mapping(bytes32 => bool) public cancelledOrders;
    
    modifier onlyVerifiedContract(address nftContract) {
        require(verifiedContracts[nftContract], "Unverified NFT contract");
        _;
    }
    
    function secureOrderMatching(
        Order memory order,
        bytes memory signature
    ) external onlyVerifiedContract(order.nftContract) {
        bytes32 orderHash = getOrderHash(order);
        
        // Prevent replay attacks
        require(!cancelledOrders[orderHash], "Order cancelled or fulfilled");
        
        // Verify signature
        require(verifyOrderSignature(order, signature), "Invalid signature");
        
        // Check order validity
        require(order.expirationTime > block.timestamp, "Order expired");
        require(order.maker == IERC721(order.nftContract).ownerOf(order.tokenId), "Maker not owner");
        
        // Execute trade with royalty enforcement
        executeTradeWithRoyalties(order);
        
        // Mark order as fulfilled
        cancelledOrders[orderHash] = true;
    }
}
```

Focus on vulnerabilities that could lead to royalty circumvention, marketplace exploitation, or NFT ecosystem manipulation that affects creators, platforms, and collectors."""