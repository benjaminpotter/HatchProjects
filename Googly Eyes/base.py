def setup():
    size(400, 400)

eyeX = 120
eyeY = 160
def drawEyes():
    fill(255)
    ellipse(120, 160, 100, 100)
    ellipse(280, 160, 100, 100)
    fill(0)
    ellipse(eyeX, eyeY, 40, 40)
    ellipse(eyeX + 160, eyeY, 40, 40)

def eyeMovement():
    global eyeX, eyeY
    eyeX = map(mouseX, 0, 400, 100, 150)
    eyeY = map(mouseY, 0, 400, 140, 190)

def draw():
    background(100, 100, 100)
    drawEyes()
    eyeMovement()