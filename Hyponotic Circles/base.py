noStroke()
var rotation = 5
var r = random(0, 255)
var g = random(0, 255)
var colorChange = 5
hypoSize = 30

def setColor():
    r += colorChange
    g += colorChange
    if r > 255 or r < 0:
        colorChange = -colorChange

def drawHypnos():
    for i in range(30, 0, -1):
        translate(200, 200)
        fill(0, 0, 0)
        if i % 2 == 0:
            fill(r, g, 100)
            rotate(rotation)
        else:
            rotate(-rotation)
        rect(-i * (hypoSize / 2), -i * (hypoSize / 2),
             i * hypoSize, i * hypoSize, i * hypoSize)
        resetMatrix()
    rotation += 2

def draw():
    drawHypnos()
    setColor()