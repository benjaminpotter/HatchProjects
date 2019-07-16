ballHeight = 20
maxHeight = 210
def drawBackground() :
  background(141, 217, 240)
  image(getImage("cute/GrassBlock"), 0, 320, 400, 100)

def inflatableBall():
  strokeWeight(5)
  fill(255, 255, 255)
  ellipse(200, 350-ballHeight / 2, maxHeight * 2 - ballHeight, ballHeight)

def draw() :
  drawBackground()
  inflatableBall()

def keyPressed() :
  if key == ' ' :
    ballHeight += 2
    ballHeight = constrain(ballHeight, 20, maxHeight)
