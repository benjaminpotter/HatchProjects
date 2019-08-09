area = 0
radius = 0
circum = 0

def drawCircle ():
   global area, radius, circum
   background(113, 76, 191)
   textSize(50)
   text("Area of a Circle", 26, 47)
   ellipse(200, 200, abs(200 - mouseX), abs(200 - mouseX))

def calculateCircleArea ():
   global area, radius, circum
   radius = abs(200 - mouseX)
   area = 3.14 * radius * radius
   circum = 2 * 3.14 * radius

def printOutCalculations ():
   global area, radius, circum
   textSize(15)
   text("Radius =" + str(radius), 163, 345)
   text("Area =" + str(area), 154, 362)
   text("Circumference =" + str(circum), 145, 380)

def draw ():
   drawCircle()
   calculateCircleArea()
   printOutCalculations()
