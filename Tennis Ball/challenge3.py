xPos = 0
yPos = 0
speed = 0.3

def drawBall():
   global xPos, yPos, speed
   background(109, 189, 199)
   noStroke()
   fill(181, 245, 52)
   ellipse(xPos, yPos, 300, 300)
drawBall()

def drawStitches():
   global xPos, yPos, speed
   stroke(255, 255, 255)
   strokeWeight(10)
   noFill()
   arc(xPos - 200, yPos, 275, 350, 322, 399)
   arc(xPos + 200, yPos, 275, 350, 142, 219)
drawStitches()

def draw():
   global xPos, yPos, speed
   xPos += speed
   yPos = 60 + sin(xPos/2) * -200
   drawBall()
   drawStitches()
   if xPos > 490 :
       xPos = -10
