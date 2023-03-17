**Kaarpool**



**nonce**: The nonce specification is used to keep track of the number of transactions sent from your address. We need this for security purposes and to prevent replay attacks. To get the number of transactions sent from your address we use getTransactionCount.

**transaction**: The transaction object has a few aspects we need to specify

**to**: This is the address we want to send Eth to. In this case, we are sending Eth back to the Rinkeby faucet we initially requested from.

**value**: This is the amount we wish to send, specified in wei where 10¹⁸ wei = 1 ETH

**gas**: There are many ways to determine the right amount of gas to include with your transaction. Alchemy even has a gas price webhook to notify you when the gas price falls within a certain threshold. For mainnet transactions, it’s good practice to check a gas estimator like Eth Gas Station to determine the right amount of gas to include. 21000 is the minimum amount of gas an operation on Ethereum will use, so to ensure our transaction will be executed we put 30000 here.

**maxFeePerGas**: This is the amount you are willing to pay per gas for the transaction to execute. Since EIP 1559 this field or the maxPriorityFeePerGas field is required.

**nonce**: see above nonce definition. Nonce starts counting from zero.

**data**: This is optional and used for sending additional information with your transfer, or calling a smart contract, not required for balance transfers, check out the note below.

**signedTx**: To sign our transaction object we will use the signTransaction method with our PRIVATE_KEY

**sendSignedTransaction**: Once we have a signed transaction, we can send it off to be included in a subsequent block by using sendSignedTransaction