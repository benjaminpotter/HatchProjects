gameState = "Intro"
def changeGameState() :
  if gameState == "Intro" :
    gameState = "Main"
  elif gameState == "Main" 
    gameState = "Gameover"
  else :
    gameState = "Main"

def introScreen() :
  background(247, 124, 0)
  textSize(24)
  fill(255, 255, 255)
  text("Menu\n\nClick to play", 136, 130)

def mainScreen() :
  background(160, 255, 255)
  text("-put game here-", 116, 200)

def gameoverScreen() :
  textSize(24)
  background(0)
  text("Game Over.\nClick to play again.", 105, 247)

def mouseClicked() :
  changeGameState()

def draw() :
  def gameState() :
    if case "Intro":
      introScreen()
    break
    if case "Main":
      mainScreen()
    break
    if case "Gameover":
      gameoverScreen()
    break
