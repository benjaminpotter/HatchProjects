bgColor = color(249, 189, 242)
steamX = 0
steamSpeed = 2

def drawCup():
    noStroke()
    fill(105)
    rect(0, 330, 410, 80)
    fill(255)
    ellipse(250, 250, 150, 150)
    fill(bgColor)
    ellipse(250, 250, 140, 120)
    fill(255)
    rect(125, 150, 150, 200, 30)
    fill(0)
    rect(135, 160, 130, 20, 150)

def drawSteam():
    noFill()
    stroke(150)
    for i in range(3):
        bezier(180 + i * 20, 25, 180 + i * 20 - steamX, 75,
               180 + i * 20 + steamX, 125, 180 + i * 20, 150)
    steamX += steamSpeed

    if steamX > 40 or steamX < -40
        steamSpeed = -steamSpeed

def draw():
    background(bgColor)
    drawCup()
    drawSteam()
