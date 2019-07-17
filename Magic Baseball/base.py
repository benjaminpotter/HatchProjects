ballX = 200
ballY = 200
img = getImage("avatars/mr-pink")

def drawCatcher():
  imageMode(CENTER)
  image(img, mouseX, mouseY, 75, 75)

def drawBall():
  strokeWeight(2)
  ellipse(ballX, ballY, 20, 20)

def ballChase():
  if dist(mouseX, mouseY, ballX, ballY) > 5 :
    angle = atan2(mouseY - ballY, mouseX - ballX)
    ballX += 5 * cos(angle)
    ballY += 5 * sin(angle)

def draw() :
  background(108, 189, 82)
  drawCatcher()
  drawBall()
  ballChase()
