# Lottery
We will deploy and interact with a lottery contract to the Ethereum blockchain (using Ganache because we do not want to spend any ETH it's a test).
We use the REMIX IDE to deploy the contract, then using Web3.py, we interact with the deployed contract.
First, when we use Remix to deploy the contract, we can actually see the transaction and the contract which instanciate it thanks to the graphical interface of Ganache.
After that ww can observe that all the accounts have 100 ETH: this is the beginning of the lottery.
When the accounts have sent their ETH (1 per account, we actually request the contract 5 time), we can see that the logic has occurs and the crypto has been sent to the winner (and to the owner of the contract, because it was coded in the logic).
