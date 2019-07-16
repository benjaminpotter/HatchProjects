import datetime

arms = {}

textAlign(CENTER, CENTER)
textSize(16)
def drawArm(degrees, length, weight):
    pushMatrix()
    translate(200, 200)
    rotate(degrees - 90)
    strokeWeight(weight)

    line(-length / 10, 0, length, 0)
    popMatrix()

def drawNumbers():
    strokeWeight(2)
    fill(0)
    for i in range(1, 60):
        angle = PI / 6 * (i / 5 - 3)
        if i % 5 == 0:
            text(i / 5, 200 + cos(angle) * 140, 200 + sin(angle) * 140)
        else:
            point(200 + cos(angle) * 140, 200 + sin(angle) * 140)

def drawClock():
    fill(255)
    ellipse(200, 200, 300, 300)

    drawArm(arms.hour * 30, 80, 3)
    drawArm(arms.minute * 6, 100, 2)
    drawArm(arms.second * 6, 120, 1)

def updateClock():
    t = datetime.datetime.now()
    arms = {'hour': t.hour, 'minute': t.minute, 'second': t.second}

    arms['minute'] += arms['second'] / 60
    arms['hour'] += arms['minute'] / 60

def draw():
    background(51)
    updateClock()
    drawClock()
    drawNumbers()