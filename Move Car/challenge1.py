xPosition = 275
yPosition = 275
xSpeed = 2

def drawBackground():
   noStroke()
   background(125, 255, 255)
   fill(68, 255, 0)
   rect(0,200,400,200)
   fill(119, 119, 119)
   rect(0, 230, 400, 60)
   fill(255, 255, 0)
   rect(0, 258, 400, 5)

def drawCar():
   global xPosition
   global yPosition
   fill(255, 0, 0)
   rect(xPosition, yPosition - 10, 40, 10)
   rect(xPosition + 10, yPosition - 20, 20, 10)
   fill(0, 0, 0)
   ellipse(xPosition + 10, yPosition, 10, 10)
   ellipse(xPosition + 30, yPosition, 10, 10)

def moveCar():
   global xPosition
   global xSpeed
   xPosition += xSpeed

def loopCar():
   global xPosition
   global xSpeed
   if xPosition > 400 :
       xPosition = 0
  

def draw():
   drawBackground()
   drawCar()
   moveCar()
   loopCar()
