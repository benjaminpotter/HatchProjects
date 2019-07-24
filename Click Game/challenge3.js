var start = millis();
var score = 0;
var counter = 0;

var displayGame = function() {
  background(0, 252, 0);
  textSize(16);
  text("Click and hold when the number is a multiple of 3", 50, 50);
  textSize(20);
  text("Score: " + score, 165, 350);
  textSize(90);
  text(counter, 185, 200);
};

var countUp = function() {
  counter = round((millis() - start) / 1000);
};

var addScore = function() {
    if (counter % 3 === 0) {
      score++;
    } else {
      score--;
    }            
};

var winScreen = function() {
  background(86, 74, 255);
  textSize(37);
  text("You won in " + counter + " seconds!", 10, 200);
};

var draw = function() {
  if (score < 100) {
    displayGame();
    countUp();       
  } else {
    winScreen();
  }
};

var keyPressed = function() {
  if (keyCode === 32) {
      addScore();
  }  
};
