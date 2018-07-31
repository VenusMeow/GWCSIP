//a function to display the current time
function displayDate() {
    document.getElementById("clock").innerHTML = Date();
}

//a function to play the rock paper scissors game
function rps() {
  var result = "";
  var user = document.getElementById("input").value;
  //console.log(user);   (for debugging)
  var computer = Math.floor((Math.random() * 3) + 1);
  //console.log(computer);  (for debugging)
  if (user==1){
    if(computer==1){
      result = "I chose rock, that's a tie!";
    } else if (computer==2){
      result = "I chose paper, I win!";
    } else {
      result = "I chose scissors, you win!";
    }
  } else if (user==2){
    if(computer==1){
      result = "I chose rock, you win!";
    } else if (computer==2){
      result = "I chose paper, that's a tie!";
    } else {
      result = "I chose scissors, I win!";
    }
  } else if (user==3) {
    if(computer==1){
      result = "I chose rock, I win!";
    } else if (computer==2){
      result = "I chose paper, you win!";
    } else {
      result = "I chose scissors, that's a tie!";
    }
  } else {
    result = "You need to input either 1, 2 or 3!";
  }
  document.getElementById("result").innerHTML = result;
}
