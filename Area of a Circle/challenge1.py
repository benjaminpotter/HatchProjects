area = 0
radius = 0

def drawCircle():
   global area, radius
   background(113, 76, 191)
   textSize(50)
   text("Area of a Circle", 26, 47)
   ellipse(200, 200, abs(200 - mouseX), abs(200 - mouseX))

def calculateCircleArea():
   global area, radius
   radius = abs(200 - mouseX)
   area = 3.14 * radius * radius

def printOutCalculations():
   global area, radius
   textSize(15)
   text("Radius = " + str(radius), 163, 345)
   text("Area = " + str(area), 154, 362)

def draw():
   global area, radius
   fill(radius, radius, radius)
   drawCircle()
   calculateCircleArea()
   printOutCalculations()
