def setup():
    size(400, 400)
    noStroke()

rotation = 5
r = random(0, 255)
g = random(0, 255)
colorChange = 5
hypoSize = 30

def setColor():
    global colorChange, r, g
    r += colorChange
    g += colorChange
    if r > 255 or r < 0:
        colorChange = -colorChange

def drawHypnos():
    global rotation
    global r, g
    global hypoSize
    
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

    rotation += 0.05

def draw():
    drawHypnos()
    setColor()