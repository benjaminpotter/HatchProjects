numOfLines = 30
speed = 1
pos = 1
lineColor = color(0)
backgroundColor = color(255)
dark = False

def drawLines():
    for i in range(numOfLines):
        stroke(lineColor)
        strokeWeight(13)
        rect(i * 20, -1, 0, 401)

def drawSquares():
    noStroke()
    fill(0)
    rect(pos, 130, 100, 50)
    fill(255)
    rect(pos, 230, 100, 50)

def animateSquares():
    global pos, speed
    if pos <= 0 or pos >= 300:
        speed *= -1
    pos += speed

def keyPressed():
    global dark, backgroundColor, lineColor
    if key == ' ' and dark == False:
        backgroundColor = color(50)
        lineColor = color(100)
        dark = True
    elif key == ' ' and dark == True:
        backgroundColor = color(255)
        lineColor = color(0)

def draw():
    background(backgroundColor)
    drawLines()
    drawSquares()
    animateSquares()