gameover = false

def drawGame() :
  background(255, 255, 255);
  fill(232, 0, 0);
  textSize(20);
  text("Don't click the screen or you lose.", 50, 40);

def drawGameover() :
  background(0, 0, 0)
  fill(232, 0, 0)
  textSize(20)
  text("YOU LOSE", 160, 210)

def draw() :
  if !gameover :
    drawGame()
  else :
    drawGameover();

def mouseClicked() :
  gameover = true
