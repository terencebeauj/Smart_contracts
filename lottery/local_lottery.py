from web3 import Web3
import json

local_endpoint = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(local_endpoint))

contract_address = "0x2Ab8fc3A0e1a44A54953D6b8134414498B719154"

contract_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pickWinner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"players","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"random","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]')

lottery = w3.eth.contract(address=contract_address, abi=contract_abi)

print(f" Manager address: {lottery.functions.manager().call()}")

sender_1 = "0xf9D6cF6B163Db81dC78aA73874C8921fC0266D4D"
private_key_1 = "860b2da53e0f4316a18a0707da55d9bd0d5d6ed108c5b0102e5d2b164395e254"
sender_2 = "0x0A30F83A9Bcc05438F940665Ce0df55E1D947D8a"
private_key_2 = "20590528440ebf0e6ea9801b2f08a4baf061f08d1ed943992948178c4fd60f8c"
sender_3 = "0x79C5DeDE3ff331f90801E241DeaB6478F4679e54"
private_key_3 = "34a8a5dc86c1d7f81e6a1a026adbe61dbad11135230ceaeb9cdd45bb9b6cdad6"
sender_4 = "0x9a91845533F684a785dd4C6cBd0ee55E7D8Bf188"
private_key_4 = "e07fe33147177648df12be0e95833d4eee3b7d09e19cf09adc5ddf20c0309fe4"

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

# for i in range(5):
#     print(f"Participant {i+1}: {lottery.functions.players(i).call()}")

tx = lottery.functions.pickWinner().buildTransaction({
    "gas": 700000,
    "gasPrice": w3.toWei(1, "gwei"),
    "from": "0x2Cea03DDc6b821e143B1Ce0D3851a8D9334737ca",
    "nonce": w3.eth.getTransactionCount("0x2Cea03DDc6b821e143B1Ce0D3851a8D9334737ca")
})

private_key = "5a7713daa0c60454ceddd3e7256ce3e0192d7f84240047814064aa367726e4a9"

signed_tx = w3.eth.account.sign_transaction(tx, private_key)

tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

balance = w3.fromWei(lottery.functions.getBalance().call(), "ether")
print(f"The actual balance of the lottery is: {balance} ether")