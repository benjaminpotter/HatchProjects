gravity = 1
velocityY = 0
posY = 20
posX = 200
def drawScene():
  background(237, 237, 228)
  fill(0, 0, 255)
  ellipse(posX,posY,20,20)

def updateBall():
  velocityY += gravity
  posY += velocityY

def moveBallHorizontally():
  if keyIsPressed :
    if keyCode == LEFT :
      posX -= 3
  elif keyCode == RIGHT :
      posX += 3

def bounceBall():
  if posY > 390 :
    posY = 390
    velocityY = -velocityY

def draw():
  drawScene()
  updateBall()
  moveBallHorizontally()
  bounceBall()
