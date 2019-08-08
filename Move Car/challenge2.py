xPosition = 275
yPosition = 275
xSpeed = 2

def drawBackground():
   noStroke()
   background(125, 255, 255)
   fill(68, 255, 0)
   rect(0,200,400,200)

def drawCar():
   global xPosition
   global yPosition 
   global xSpeed
   fill(255, 0, 0)
   rect(xPosition, yPosition - 10, 40, 10)
   rect(xPosition + 10, yPosition - 20, 20, 10)
   fill(0, 0, 0)
   ellipse(xPosition + 10, yPosition, 10, 10)
   ellipse(xPosition + 30, yPosition, 10, 10)

def draw():
   global xPosition
   global yPosition
   global xSpeed
   drawBackground()
   drawCar()
   if keyIsPressed and keyCode == RIGHT_ARROW :
       xPosition += 2
  
   if keyIsPressed and keyCode == LEFT_ARROW :
       xPosition -= 2
  
   if xPosition > 400 :
       xPosition = 0
  
   if xPosition < 0 :
       xPosition = 400
