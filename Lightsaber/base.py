xPos = 202
yPos = 300
speed = 15
noStroke()
rectMode(CORNERS)

def drawHilt():
    fill(189, 189, 189)
    rect(200, 300, 214, 378)
    fill(255, 0, 0)
    ellipse(214, 325, 6, 15)

def drawBeam():
    fill(186, 255, 231)
    rect(xPos, yPos, 211, 340)
    fill(0, 255, 204)
    rect(xPos, yPos, 207, 320)
    yPos -= speed
    if yPos < 50:
        yPos = 50

def draw():
    background(255, 255, 255)
    if mouseIsPressed:
        drawBeam()
    else:
        yPos = 300
    drawHilt()
