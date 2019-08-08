xPosition1 = 0
yPosition1 = 275
xSpeed1 = 2
xPosition2 = 400
yPosition2 = 275
xSpeed2 = 2

def drawBackground():
   global xPosition1
   global yPosition1
   global xSpeed1
   global xPosition2
   global yPosition2
   global xSpeed2
   noStroke()
   background(125, 255, 255)
   fill(68, 255, 0)
   rect(0, 200, 400, 200)

def drawCar1():
   global xPosition1
   global yPosition1
   global xSpeed1
   global xPosition2
   global yPosition2
   global xSpeed2
   fill(255, 0, 0)
   rect(xPosition1, yPosition1 - 10, 40, 10)
   rect(xPosition1 + 10, yPosition1 - 20, 20, 10)
   fill(0, 0, 0)
   ellipse(xPosition1 + 10, yPosition1, 10, 10)
   ellipse(xPosition1 + 30, yPosition1, 10, 10)

def drawCar2():
   global xPosition1
   global yPosition1
   global xSpeed1
   global xPosition2
   global yPosition2
   global xSpeed2
   fill(0, 0, 255)
   rect(xPosition2, yPosition2 - 10, 40, 10)
   rect(xPosition2 + 10, yPosition2 - 20, 20, 10)
   fill(0, 0, 0)
   ellipse(xPosition2 + 10, yPosition2, 10, 10)
   ellipse(xPosition2 + 30, yPosition2, 10, 10)

def moveCar2():
   global xPosition1
   global yPosition1
   global xSpeed1
   global xPosition2
   global yPosition2
   global xSpeed2
   xPosition2 -= xSpeed2

def loopCar2():
   global xPosition1
   global yPosition1
   global xSpeed1
   global xPosition2
   global yPosition2
   global xSpeed2
   if xPosition2 < 0 :
    xPosition2 = 400
  

def draw():
   global xPosition1
   global yPosition1
   global xSpeed1
   global xPosition2
   global yPosition2
   global xSpeed2
   drawBackground()
   drawCar1()
   if keyIsPressed and keyCode == RIGHT_ARROW :
       xPosition1 += 2
  
   if keyIsPressed and keyCode == LEFT_ARROW :
       xPosition1 -= 2
       
   if keyIsPressed and keyCode == UP_ARROW :
       yPosition1 -= 2
  
   if keyIsPressed and keyCode == DOWN_ARROW :
       yPosition1 += 2
  
   if xPosition1 > 400 :
       xPosition1 = 0
  
   if xPosition1 < 0 :
       xPosition1 = 400
  
   drawCar2()
   moveCar2()
   loopCar2()
   if xPosition1 - xPosition2 > -20 and yPosition1 - yPosition2 > -10 :
       xSpeed2 = 0
       xSpeed1 = 0
       textAlign(CENTER)
       textSize(40)
       fill(255, 0, 0)
       text("Game Over", 200, 150)
