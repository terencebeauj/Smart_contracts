//SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.5.0 <0.9.0;

// This contract is an implementable lottery, i.e that you can receive a fixed amount of ETH and then choose a winner amongst the candidates, and send him all the ETH.

contract Lottery{
    address payable[] public players;
    address public manager;

    constructor(){
        manager = msg.sender;
    }

// Function for receive ether from external sources (EOA or contracts)
    receive() external payable{
        require(msg.value == 1 ether && msg.sender != manager);
        players.push(payable(msg.sender));
    }

// Get the amount of the lottery
    function getBalance() public view returns(uint){
        // require(msg.sender == manager);
        return address(this).balance;
    }

// Generate a PSEUDO-random number
    function random() public view returns(uint){
        return uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players.length)));

    }

// Function to select the winner of the lottey, all the ether will be send to him through the blockchain
    function pickWinner() public{
        // If there are at least 2 players, then anyone can execute this function
        if(players.length >= 2){
            players.push(payable(manager)); // add the manager to the lottery automatically

            uint r = random();
            address payable winner;

            uint index = r % players.length;
            winner = players[index];

            uint fees = getBalance()*10/100;// get 10% of the balance

            payable(manager).transfer(fees);// transfert the fees for the manager

            winner.transfer(getBalance());

            players = new address payable[](0);

        }

        // Otherwise, only the manager can execute it
        else{
            require(msg.sender == manager);
            players.push(payable(manager)); // add the manager to the lottery automatically

            uint r = random();
            address payable winner;

            uint index = r % players.length;
            winner = players[index];

            uint fees = getBalance()*10/100;

            payable(manager).transfer(fees);

            winner.transfer(getBalance());

            players = new address payable[](0);
        }
    }
}
