from web3 import Web3

provider_url = "https://goerli.infura.io/v3/5dbe132c0e924bcb8d2e1185672b9c9a"
w3 = Web3(Web3.HTTPProvider(provider_url))


def print_eth_detail(account="0x82e48CA339c2694251614392494DEa7cc9756D12"):
    # print ETH details
    print(f'Hi, {w3.isConnected()}')  # connection
    print("Latest block is", w3.eth.get_block("latest"))
    print("Address is", w3.isAddress("0x82e48CA339c2694251614392494DEa7cc9756D12"))

    # ETH Balance
    wallet = w3.toChecksumAddress("0x82e48CA339c2694251614392494DEa7cc9756D12")
    balance = w3.eth.get_balance(wallet)
    print("Wallet WEI Balance = WEI", balance)

    # Wei to ETH
    ethBalance = w3.fromWei(balance, "ether")
    print("Wallet ETH Balance = ETH", ethBalance)

    return ethBalance


def send_eth(account="0x82e48CA339c2694251614392494DEa7cc9756D12"):
    # ganache_url = 'IMPORTYOURURL'
    # web3 = Web3(Web3.HTTPProvider(ganache_url))
    account_1 = w3.toChecksumAddress("0x82e48CA339c2694251614392494DEa7cc9756D12")
    private_key1 = '508e0795d166bc7dc0d68097387fa31f1d3e01662b92f0281ff909c8b29d9f23'
    account_2 = w3.toChecksumAddress("0x991C6e0611A0a625902d6815E2FcE0A7DD8135D1")

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


def send_eth_api(amountInINR, driverAccount="0x82e48CA339c2694251614392494DEa7cc9756D12", riderAccount="0x82e48CA339c2694251614392494DEa7cc9756D12"):
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

    # 1 INR = 0.000007272  ETH
    amountInETH = amountInINR * 0.000007272
    driverAccount = w3.toChecksumAddress(driverAccount)
    private_key1 = '508e0795d166bc7dc0d68097387fa31f1d3e01662b92f0281ff909c8b29d9f23'
    riderAccount = w3.toChecksumAddress("0x991C6e0611A0a625902d6815E2FcE0A7DD8135D1")

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
    print_eth_detail('PyCharm')
