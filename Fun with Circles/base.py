firstClick = True
xPoint = 0
yPoint = 0

def saveMousePosition():
    xPoint = mouseX
    yPoint = mouseY

def mouseClicked():
    global firstClick
    
    if firstClick == True:
        fill(random(0, 255), random(0, 255), random(0, 255))
        saveMousePosition()
        firstClick = False
    else:
        firstClick = True

def drawCircle():
    if firstClick == False:
        ellipseMode(CENTER)
        ellipse(xPoint, yPoint, (mouseX - xPoint) * 2, (mouseY - yPoint) * 2)

def draw():
    drawCircle()
