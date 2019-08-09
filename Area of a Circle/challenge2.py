area = 0
radius = 0
areaCanv = 0

def drawCircle ():
   global radius, area, areaCanv
   background(113, 76, 191)
   textSize(50)
   text("Area of a Circle", 26, 47)
   ellipse(200, 200, abs(200 - mouseX), abs(200 - mouseX))

def calculateCircleArea ():
   global radius, area, areaCanv
   radius = abs(200 - mouseX)
   area = 3.14 * radius * radius
   areaCanv = 160000 - area

def printOutCalculations ():
   global radius, area, areaCanv
   textSize(15)
   text("Radius = " + str(radius), 163, 345)
   text("Area of Circle = " + str(area), 154, 362)
   text("Area of Canvas = " + str(areaCanv), 140, 380)

def draw ():
   global radius, area, areaCanv
   drawCircle()
   calculateCircleArea()
   printOutCalculations()
