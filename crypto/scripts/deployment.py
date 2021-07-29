from brownie import Crypto, config, accounts

def main():
    account = accounts.add(config["wallets"]["key_1"])
    return Crypto.deploy({"from": account})