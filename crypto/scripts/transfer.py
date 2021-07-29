from brownie import Crypto, config, accounts

def main():
    account1 = accounts.add(config["wallets"]["key_1"])
    account2 = "0xb5c6DDc9E860FB11406fc76c91B1C70962eF0503"
    return Crypto[0].transfer(account2, 100, {"from": account1})