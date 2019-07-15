def setup():
    size(400, 400)
    background(0)
    noStroke()
    fill(255)
    dots()

sleep = [8, 7.7, 6, 6.5, 5.5, 8, 9, 11, 3, 4, 5, 10]
xPos = 0
yPos = 200
circleSize = 10

def calculateDistance(i):
    global sleep, yPos
    if sleep[i] > sleep[i - 1]:
        yPos = yPos - sleep[i] * 5
    else:
        yPos = yPos + sleep[i] * 5

def calculateSize(i):
    global sleep, circleSize
    if sleep[i] > sleep[i - 1]:
        circleSize = random(15, 20)
    else:
        circleSize = random(2, 15)

def dots():
    global sleep, yPos
    for i in range(len(sleep)):
        translate(370 / len(sleep), 0)
        calculateDistance(i)
        calculateSize(i)
        ellipse(0, yPos, circleSize, circleSize)