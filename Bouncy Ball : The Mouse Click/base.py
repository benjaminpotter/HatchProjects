xPos = random(0, 400)
yPos = random(0, 400)
xSpeed = 5
ySpeed = 5
def movingBall() :
  fill(66, 66, 66)
  ellipse(xPos, yPos, 20, 20)
  xPos = xPos + xSpeed  
  yPos = yPos + ySpeed

def ballBounce() :
  if xPos < 0 or xPos > 400 :
    xSpeed = -xSpeed
  if yPos < 0 or yPos > 400 :
    ySpeed = -ySpeed

def mouseClicked() :
 xPos = mouseX
 yPos = mouseY
 xSpeed = random(-5, 5)
 ySpeed = random(-5, 5)

def draw() :
  background(127, 204, 255)
  movingBall()
  ballBounce()
