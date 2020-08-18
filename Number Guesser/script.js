// Weronika, 17/08/2020

let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
function generateTarget(){
//This function should return a random integer between 0 and 9.
  return Math.floor(Math.random()*10);
};

function compareGuesses(humanGuess, computerGuess, currentTargetNumber){
//This function will be called each round to determine which guess is closest to the target number.
  if (humanGuess > 10){
    alert("You have entered invalid number");
  } else {
    if ((Math.abs(currentTargetNumber - computerGuess)) < (Math.abs(currentTargetNumber - humanGuess))){
      return false;
    } else {
      return true;
    };
  };  
};

function updateScore(winner) {
//This function will be used to correctly increase the winner’s score after each round.
  if (winner === "human") {
    humanScore++;
  } else if (winner === 'computer') {
    computerScore++;
  };
};

function advanceRound(){
// This function will be used to update the round number after each round.
  currentRoundNumber++;
};

