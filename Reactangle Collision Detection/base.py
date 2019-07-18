imgW = 200
imgH = 150
imgX = 200
imgY = 200
ballRadius = 25
horizontalOverlap = False
verticalOverlap = False

def drawScene():
    background(112, 181, 85)
    imageMode(CENTER)
    image(getImage("avatars/marcimus"), imgX, imgY, imgW, imgH)
    stroke(0, 0, 0)
    strokeWeight(2)
    fill(255, 255, 255)
    ellipse(mouseX, mouseY, ballRadius * 2, ballRadius * 2)

def drawGuidelines():
    stroke(0, 0, 0)
    line(imgX - imgW / 2, 0, imgX - imgW / 2, 400)
    line(imgX + imgW / 2, 0, imgX + imgW / 2, 400)
    line(0, imgY - imgH / 2, 400, imgY - imgH / 2)
    line(0, imgY + imgH / 2, 400, imgY + imgH / 2)
    stroke(255, 0, 0)
    noFill()
    rectMode(CENTER)
    rect(imgX, imgY, imgW, imgH)
    rect(mouseX, mouseY, 50, 50)

def checkOverlap():
    leftSide = mouseX + ballRadius > 200 - imgW / 2
    rightSide = mouseX - ballRadius < 200 + imgW / 2
    topSide = mouseY + ballRadius > 200 - imgH / 2
    bottomSide = mouseY - ballRadius < 200 + imgH / 2
    horizontalOverlap = leftSide and rightSide
    verticalOverlap = topSide and bottomSide

def checkCollision():
    if horizontalOverlap and verticalOverlap:
        textSize(50)
        textAlign(CENTER, CENTER)
        text("Colliding!", 200, 75)

def draw():
    drawScene()
    drawGuidelines()
    checkOverlap()
    checkCollision()