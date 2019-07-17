man = 0
motion = 5

def stickman(man):
    stroke(0, 0, 0)
    fill(148, 148, 78)
    ellipse(200, man + 200, 20, 20)
    line(200, man + 210, 200, man + 250)
    line(200, man + 230, 178, man + 213)
    line(200, man + 230, 222, man + 213)
    line(200, man + 250, 185, man + 272)
    line(200, man + 250, 215, man + 272)

def drawPortals():
    textSize(50)
    fill(random(0, 225))
    text("INFINITE\n PORTAL", 95, 193)
    strokeWeight(2)
    noStroke()
    fill(242, 186, 19)
    ellipse(200, 43, 259, 21)
    fill(17, 0, 255)
    ellipse(200, 350, 259, 18)
    strokeWeight(2)
    stroke(0, 0, 0)
    line(0, 60, 400, 60)
    line(0, 335, 400, 335)

def drawOcclusion():
    fill(255, 255, 255)
    stroke(255, 255, 255)
    rect(0, -10, 400, 40)
    rect(0, 360, 400, 40)

def moveMan():
    global man, motion
    
    man += motion
    if man > 170:
        man = -162

def draw():
    background(255)
    drawPortals()
    stickman(man)
    stickman(man - 332)
    drawOcclusion()
    moveMan()
