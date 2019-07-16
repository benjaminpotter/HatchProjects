trailLength = 3
trackX = []
trackY = []
lastMouseX = mouseX
lastMouseY = mouseY

def drawTrail():
    stroke(255, 115, 0)
    strokeWeight(30)
    line(mouseX, mouseY, lastMouseX, lastMouseY)

def drawBaseball():
    stroke(0, 0, 0)
    strokeWeight(3)
    ellipse(mouseX, mouseY, 40, 40)

def trackMouse():
    trackX.push(mouseX)
    trackY.push(mouseY)

def updateTrail():
    if len(trackX) > trailLength:
        index = len(trackX) - 1 - trailLength
        lastMouseX = trackX[index]
        lastMouseY = trackY[index]
        trackX.shift()
        trackY.shift()

def draw():
    background(169, 222, 219)
    drawTrail()
    drawBaseball()
    trackMouse()
    updateTrail()