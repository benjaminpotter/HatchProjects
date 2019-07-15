def setup():
    size(400, 400)

threePoint = 0
fieldGoal = 0
freeThrow = 0

shotclock = 24000
lastShot = 0

def drawScoreboard():
    global threePoint, fieldGoal, freeThrow

    background(0, 0, 0)
    noFill()
    stroke(255, 0, 0)
    rect(30, 337, 110, 34)
    rect(155, 337, 110, 34)
    rect(278, 337, 116, 34)
    textSize(22)
    fill(threePoint * 1.2 + 30, fieldGoal * 1.3 + 30, freeThrow * 1.8 + 30)
    text("3-Point", 50, 361)
    text("Field Goal", 160, 361)
    text("Free Throw", 279, 361)
    textSize(150)
    fill(255)
    text(threePoint * 3 + fieldGoal * 2 + freeThrow, 116, 200)


def addPoints():
    global threePoint, fieldGoal, freeThrow
    
    if mouseX > 30 and mouseX < 140 and mouseY > 337 and mouseY < 371:
        threePoint += 1
        resetClock()
    elif mouseX > 155 and mouseX < 265 and mouseY > 337 and mouseY < 371:
        fieldGoal += 1
        resetClock()
    elif mouseX > 278 and mouseX < 388 and mouseY > 337 and mouseY < 371:
        freeThrow += 1
        resetClock()

def resetClock():
    global shotclock, lastShot
    lastShot = millis()

def draw():
    drawScoreboard()
    
    global shotclock, lastShot
    timeSinceLastShot = millis() - lastShot
    shotclock = timeSinceLastShot
    
    if shotclock >= 24000:
        resetClock()
        
    fill(255)
    textSize(22)
    text(shotclock/1000, 10, 30)

def mousePressed():
    addPoints()