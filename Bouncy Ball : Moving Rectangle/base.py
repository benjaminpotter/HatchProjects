xPos = random(0,400) 
yPos = random(0,400)
xSpeed = 5     
ySpeed = 5
rectX = 150
rectY = 150
rectWidth = 80
rectHeight = 100


def movingBall () :
  fill(66, 66, 66)
  ellipse(xPos, yPos, 20, 20)
  xPos = xPos + xSpeed  
  yPos = yPos + ySpeed

def drawRectangle () : 
  fill(35, 60, 112)
  rect(rectX,rectY,rectWidth,rectHeight)

def ballBounce () :
  if xPos < 0 or xPos > 400 :
    xSpeed = -xSpeed

  if yPos < 0 or yPos > 400 :
    ySpeed = -ySpeed

def bounceOffRectangle () :
  if xPos > rectX - 3 and xPos < rectX + rectWidth + 3 and yPos > rectY - 3 and yPos < rectY + rectHeight + 3 :
    if xPos < rectX + 3 or xPos > rectX + rectWidth - 3 :
      xSpeed = -xSpeed
    elif yPos < rectY + 3 or yPos > rectY + rectHeight - 3 :
      ySpeed = -ySpeed

def mouseClicked () :
 xPos = mouseX
 yPos = mouseY
 xSpeed = random(-5,5)
 ySpeed = random(-5,5)

def mouseDragged () :
  rectX = mouseX - rectWidth/2
  rectY = mouseY - rectHeight / 2

def draw () :
  background(127, 204, 255)
  movingBall()
  ballBounce()
    drawRectangle()
    bounceOffRectangle()
