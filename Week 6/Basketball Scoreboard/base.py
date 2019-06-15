def setup():
    size(400, 400)

threePoint = 0
fieldGoal = 0
freeThrow = 0

def drawScoreboard():
    global threePoint, fieldGoal, freeThrow

    background(0, 0, 0)
    noFill()
    stroke(255, 0, 0)
    rect(30, 337, 110, 34)
    rect(155, 337, 110, 34)
    rect(278, 337, 116, 34)
    textSize(22)
    text("3-Point", 50, 361)
    text("Field Goal", 160, 361)
    text("Free Throw", 279, 361)
    textSize(150)
    text(threePoint * 3 + fieldGoal * 2 + freeThrow, 116, 200)


def addPoints():
    global threePoint, fieldGoal, freeThrow
    
    if mouseX > 30 and mouseX < 140 and mouseY > 337 and mouseY < 371:
        threePoint += 1
    elif mouseX > 155 and mouseX < 265 and mouseY > 337 and mouseY < 371:
        fieldGoal += 1
    elif mouseX > 278 and mouseX < 388 and mouseY > 337 and mouseY < 371:
        freeThrow += 1

def draw():
    drawScoreboard()


def mousePressed():
    addPoints()