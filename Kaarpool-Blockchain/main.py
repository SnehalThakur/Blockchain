from web3 import Web3

provider_url = "https://goerli.infura.io/v3/a0c7a08733d34f85b9c872fb59088cc2"
w3 = Web3(Web3.HTTPProvider(provider_url))


def print_eth_detail_rider(account="0x1256BBcc2c63703AdeB176AAd634ba6793EeB24E"):
    # print ETH details
    print(f'Hi, {w3.isConnected()}')  # connection
    print("Latest block is", w3.eth.get_block("latest"))
    print("Address is", w3.isAddress("0x1256BBcc2c63703AdeB176AAd634ba6793EeB24E"))
    # ETH Balance
    wallet = w3.toChecksumAddress("0x1256BBcc2c63703AdeB176AAd634ba6793EeB24E")
    balance = w3.eth.get_balance(wallet)
    print("Wallet WEI Balance = WEI", balance)
    # Wei to ETH
    ethBalance = w3.fromWei(balance, "ether")
    print("Wallet ETH Balance = ETH", ethBalance)
    return ethBalance


def print_eth_detail_driver(account="0xa35948d0a9c95bA0C6C4fE97b6827D96e28Da05E"):
    # print ETH details
    print(f'Hi, {w3.isConnected()}')  # connection
    print("Latest block is", w3.eth.get_block("latest"))
    print("Address is", w3.isAddress("0xa35948d0a9c95bA0C6C4fE97b6827D96e28Da05E"))
    # ETH Balance
    wallet = w3.toChecksumAddress("0xa35948d0a9c95bA0C6C4fE97b6827D96e28Da05E")
    balance = w3.eth.get_balance(wallet)
    print("Wallet WEI Balance = WEI", balance)
    # Wei to ETH
    ethBalance = w3.fromWei(balance, "ether")
    print("Wallet ETH Balance = ETH", ethBalance)
    return ethBalance


def send_eth(account="0xa35948d0a9c95bA0C6C4fE97b6827D96e28Da05E"):
    # ganache_url = 'IMPORTYOURURL'
    # web3 = Web3(Web3.HTTPProvider(ganache_url))
    account_1 = w3.toChecksumAddress("0xa35948d0a9c95bA0C6C4fE97b6827D96e28Da05E") #driverAccount
    private_key1 = 'e72e860db9b8385e8bffd473cf2793fec76dbda0cccd5716fb7168be7545d802'
    account_2 = w3.toChecksumAddress("0x1256BBcc2c63703AdeB176AAd634ba6793EeB24E") #riderAccount

    # get the nonce.  Prevents one from sending the transaction twice
    nonce = w3.eth.getTransactionCount(account_1)

    # build a transaction in a dictionary
    tx = {
        'nonce': nonce,
        'to': account_2,
        'value': w3.toWei(0.01, 'ether'),
        'gas': 21000,
        'gasPrice': w3.toWei('40', 'gwei')
    }

    # sign the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key1)

    # send transaction
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # get transaction hash
    print(w3.toHex(tx_hash))


def send_eth_api(amountInINR, driverAccount="0x1256BBcc2c63703AdeB176AAd634ba6793EeB24E", riderAccount="0xa35948d0a9c95bA0C6C4fE97b6827D96e28Da05E"):
    # ganache_url = 'IMPORTYOURURL'
    # web3 = Web3(Web3.HTTPProvider(ganache_url))

    # ETH Balance before transaction
    riderWallet = w3.toChecksumAddress(riderAccount)
    riderBalance = w3.eth.get_balance(riderWallet)
    # Wei to ETH
    riderETHBalance = w3.fromWei(riderBalance, "ether")
    print("Rider Wallet Balance  before transaction = ", riderETHBalance)

    # ETH Balance before transaction
    driverWallet = w3.toChecksumAddress(driverAccount)
    driverBalance = w3.eth.get_balance(driverWallet)
    # Wei to ETH
    driverETHBalance = w3.fromWei(driverBalance, "ether")
    print("Driver Wallet Balance before transaction = ", driverETHBalance)

    # 1 INR = 0.000006555  ETH
    amountInETH = amountInINR * 0.000006555
    driverAccount = w3.toChecksumAddress(driverAccount)
    private_key1 = 'e72e860db9b8385e8bffd473cf2793fec76dbda0cccd5716fb7168be7545d802'
    riderAccount = w3.toChecksumAddress(riderAccount)

    # get the nonce.  Prevents one from sending the transaction twice
    nonce = w3.eth.getTransactionCount(driverAccount)

    # build a transaction in a dictionary
    tx = {
        'nonce': nonce,
        'to': riderAccount,
        'value': w3.toWei(amountInETH, 'ether'),
        'gas': 21000,
        'gasPrice': w3.toWei('40', 'gwei')
    }

    # sign the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key1)

    # send transaction
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # get transaction hash
    print(w3.toHex(tx_hash))

    # ETH Balance after transaction
    riderWallet = w3.toChecksumAddress(riderAccount)
    riderBalance = w3.eth.get_balance(riderWallet)
    # Wei to ETH
    riderETHBalance = w3.fromWei(riderBalance, "ether")
    print("Rider Wallet Balance after transaction = ", riderETHBalance)

    # ETH Balance  after transaction
    driverWallet = w3.toChecksumAddress(driverAccount)
    driverBalance = w3.eth.get_balance(driverWallet)
    # Wei to ETH
    driverETHBalance = w3.fromWei(driverBalance, "ether")
    print("Driver Wallet Balance after transaction = ", driverETHBalance)

    return riderETHBalance, driverETHBalance


if __name__ == '__main__':
    print_eth_detail_rider('PyCharm')
    print_eth_detail_driver('PyCharm')

