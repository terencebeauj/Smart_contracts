from web3 import Web3
import json

local_endpoint = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(local_endpoint))

contract_address = "0x9d1A04654F93797Fe8D8077880f15dBC426CA1a8"

contract_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pickWinner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"players","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"random","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]')

lottery = w3.eth.contract(address=contract_address, abi=contract_abi)

print(f" Manager address: {lottery.functions.manager().call()}")

sender_1 = "0xDdf08Bf14875d313Bb4bb9E29E6a1Ed4feBdcC00"
private_key_1 = "b401fd552610302c2e64842ea5a763cd905c767a54cb67ddb90d37fec66d2eee"
sender_2 = "0xA164C13E812504Bf56315329EbD0c1a805240c5D"
private_key_2 = "e30847a05d1009f9b6e15d15bf30b7c82f527d22ae0f728c860ea91ec2825f57"
sender_3 = "0x6911d1dA6d393b4b9163e54976E67B299c04bC93"
private_key_3 = "77999ab9cf315a9f97b9033ee739c10a95773275e46ee298983075ceb415dd9f"
sender_4 = "0x3AA5Fdb0440a95B20388333867C677c85BE9257a"
private_key_4 = "eb33e0fa3709b5fa3780e8c68b313625992cbf3a36cdb801960a3b6ec7a82977"

for address, key in [(sender_1, private_key_1), (sender_2, private_key_2), (sender_3, private_key_3), (sender_4, private_key_4)]:
    nonce = w3.eth.getTransactionCount(address)

    tx = {"nonce": nonce,
          "to": contract_address,
          "value": w3.toWei(1, "ether"),
          "gas": 200000,
          "gasPrice": w3.toWei(50, "gwei")
          }

    signed_tx = w3.eth.account.sign_transaction(tx, key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)

balance = w3.fromWei(lottery.functions.getBalance().call(), "ether")
print(f"The actual balance of the lottery is: {balance} ether")

tx = lottery.functions.pickWinner().buildTransaction({
    "gas": 700000,
    "gasPrice": w3.toWei(1, "gwei"),
    "from": "0xb0Dc451B45C6BB977A36dbcfcaAA50D034C3CeF6",
    "nonce": w3.eth.getTransactionCount("0xb0Dc451B45C6BB977A36dbcfcaAA50D034C3CeF6")
})

private_key = "a90610c08512233b12f085081326781c01fe74230e896ead4f122f07d9cf2e03"

signed_tx = w3.eth.account.sign_transaction(tx, private_key)

tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

balance = w3.fromWei(lottery.functions.getBalance().call(), "ether")
print(f"The actual balance of the lottery is: {balance} ether")