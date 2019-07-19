corner1 = 0
corner2 = 0
corner3 = 0
corner4 = 0
cornerSpeed = 5
mode = 1
def changeCorner():
    global mode
    global corner1, corner2, corner3, corner4
    global cornerSpeed
    if mode == 1: 
        corner1 += cornerSpeed
        if corner1 > 100 or corner1 <= 0:
            mode += 1
    if mode == 2:
        corner2 += cornerSpeed
        if corner2 > 100 or corner2 <= 0:
            mode += 1
    if mode == 3:
        corner3 += cornerSpeed
        if corner3 > 100 or corner3 <= 0:
            mode += 1
    if mode == 4:
        corner4 += cornerSpeed
        if corner4 > 100 or corner4 <= 0:
            mode = 1
            cornerSpeed = -cornerSpeed

def drawSquare():
    noStroke()
    fill(139, 137, 140)
    rect(200,200,200,200,corner1,corner2,corner3,corner4)
def draw():
    background(242,232,170)
    changeCorner()
    drawSquare()
    rectMode(CENTER) 
