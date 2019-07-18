ang = 0
speed = 0.1
def drawSky():
    noStroke()
    background(240, 247, 111)
def drawPole():
    strokeWeight(35)
    stroke(130, 74, 9)
    line((ang * 0.2) % (width + 40) - 20, height, (ang * 0.2) % (width + 40) - 20,  height - 60)
    strokeWeight(12)
    stroke(204, 146, 71)
    line(0 , height - 48 + 5 * sin(ang), width, height - 48 + 5 * sin(ang + 90))
    
def drawStickman():
    strokeWeight(5)
    stroke(0, 0, 0)
    fill(255, 255, 255)
    line(200, 162 + 80, 185 + 40 * sin(ang), 270 + 79)
    line(201, 162 + 80, 211 + 40 * sin(ang + 180), 270 + 82)
    line(200, 163 + 80, 200, 136)
    line(108, 89 + 20 * sin(ang), 200, 140)
    line(203, 140, 300, 180 + 20 * sin(ang + 90))
    ellipse(200, 100, 70, 70)

def updateAnimation():
    global ang
    global speed
    ang += speed
    speed += 0.1
def draw():
    drawSky()
    drawPole()
    drawStickman()
    updateAnimation()
    
