area = 0
radius = 0

def drawCircle():
    background(113, 76, 191)
    textSize(50)
    text("Area of a Circle", 26, 47)
    ellipse(200, 200, abs(200 - mouseX), abs(200 - mouseX))

def calculateCircleArea():
    radius = abs(200 - mouseX)
    area = 3.14 * radius * radius

def printOutCalculations():
    textSize(15)
    text("Radius =" + radius, 163, 345)
    text("Area =" + area, 154, 362)

def draw():
    drawCircle()
    calculateCircleArea()
    printOutCalculations()