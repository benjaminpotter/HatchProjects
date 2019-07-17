x = 0
gameSize = 40
game = FALSE
win = FALSE
start = FALSE
def drawShapes():
  fill(255, 255, 255)
  rect(60,170,280,gameSize)
  fill(255, 0, 0)
  rect(60,170,15,gameSize)
  fill(0, 21, 255)
  rect(325,170,15,gameSize)
  fill(74, 73, 73)
  textSize(12)
  text("Move in a straight line from red to blue",90,250)

def updateGame():
  if game == TRUE and start == TRUE :
    x = mouseX-75
    fill(50, 156, 50)
    rect(75,170,x,gameSize)
    if x>=250  :
      game = FALSE
      start = FALSE
      win = TRUE
    if win == TRUE :
      gameSize -= 5
      win = FALSE

def draw():
  background(199, 199, 199)
  drawShapes()
  updateGame()

def mouseMoved() : 
  if mouseX>75 and mouseX<90 and mouseY>170 and mouseY < 170 + gameSize :
    start= TRUE
  if mouseX>75 and mouseX<330 and mouseY>170 and mouseY < 170 + gameSize :
    game= TRUE
  else :
    game=FALSE
    start=FALSE
    x=0
