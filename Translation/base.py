def setup():
    size(400, 400)

def translateCanvas():
    translate(mouseX, mouseY)

def drawShapes():
    fill(0, 0, 0)
    text("(0,0)", -12, -20)
    ellipse(0, 0, 30, 30)
    text("(100,100)", 100 - 25, 100 - 20)
    ellipse(100, 100, 30, 30)
    noFill()
    rect(0, 0, 400, 400)

def draw():
    background(181, 215, 224)
    drawShapes()

def mousePressed():
    resetMatrix()
    translateCanvas()