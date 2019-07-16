ballHeight = 390
vUp = 4
aG = -0.5
time = 1
def drawTennisBall() :
  fill(27, 224, 34)
  ellipse(200, ballHeight, 20, 20)

def calculateBallPosition() :
  ballHeight -= vUp * time + 0.5 * aG * time * time
  time += 0.5

def resetBall() :
  if ballHeight > 390 :
    ballHeight = 390
    time = 1

def draw() :
  background(80, 201, 222)
  drawTennisBall()
  calculateBallPosition()
  resetBall()
