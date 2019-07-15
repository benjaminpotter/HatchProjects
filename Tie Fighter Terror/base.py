spin = 0
lastMouseX = mouseX
rectMode(CENTER)

def moveShip():
    spin = (mouseX - lastMouseX) * 2
    translate(mouseX, mouseY)
    rotate(spin)
    scale(mouseY / 200)
    translate(-200, -200)

def drawShip():
    fill(70, 70, 70)
    rect(200, 200, 100, 20)
    rect(150, 200, 20, 100)
    rect(250, 200, 20, 100)
    ellipse(200, 200, 60, 60)
    fill(0, 0, 0)
    ellipse(200, 200, 40, 40)

def draw():
    background(16, 19, 24)
    moveShip()
    drawShip()
    resetMatrix()