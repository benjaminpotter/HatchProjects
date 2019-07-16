xPos = random(0, 400)
yPos = random(0, 400)
xSpeed = 5
ySpeed = 5
def movingBall() :
  fill(66, 66, 66)
  ellipse(xPos, yPos, 20, 20)
  xPos = xPos + xSpeed
  yPos = yPos + ySpeed

def drawRectangle() : 
  fill(35, 60, 112)
  rect(150, 150, 100, 100)

def ballBounce() :
  if xPos < 0 or xPos > 400 :
    xSpeed = -xSpeed;

  if yPos < 0 or yPos > 400 :
    ySpeed = -ySpeed

def bounceOffRectangle() :
	if xPos > 145 and xPos < 255 and yPos > 145 and yPos < 255 :
		if xPos < 153 or xPos > 247 :
			xSpeed = -xSpeed;
		elif yPos < 153 or yPos > 247 :
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
    drawRectangle()
    bounceOffRectangle()
