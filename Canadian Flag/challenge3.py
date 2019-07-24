yPos = 400
ySpeed = 3

def stripes():
    fill(255, 0, 0)
    rect(0, 0, 50, 400)
    rect(350, 0, 50, 400)
def mapleLeaf():
    beginShape()
    vertex(200, 270)
    vertex(150, 273)
    vertex(155, 256)
    vertex(105, 205)
    vertex(115, 195)
    vertex(110, 160)
    vertex(135, 165)
    vertex(143, 150)
    vertex(170, 180)
    vertex(163, 110)
    vertex(180, 120)
    vertex(200, 80)
    vertex(220, 120)
    vertex(238, 110)
    vertex(230, 180)
    vertex(257, 150)
    vertex(265, 165)
    vertex(290, 160)
    vertex(285, 195)
    vertex(295, 205)
    vertex(245, 256)
    vertex(250, 273)
    endShape(CLOSE)
    stroke(255, 0, 0)
    strokeWeight(10)
    line(200, 200, 200, 300)

def printText():
    global yPos
    textAlign(CENTER)
    fill(0, 0, 0)
    textSize(30)
    strokeWeight(0)
    text("O Canada", 200, yPos)
    yPos = yPos - ySpeed
    if yPos < 0:
       yPos = 400

def draw():
    background(255, 255, 255)
    stripes()
    mapleLeaf()
    printText()
    noStroke()
