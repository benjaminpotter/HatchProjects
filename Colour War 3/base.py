RedArr = []
GrnArr = []
BluArr = []

def colorBattlefield(x):
    for y in range(40):
        RedArr[x][y] = random(0, 255)
        GrnArr[x][y] = random(0, 255)
        BluArr[x][y] = random(0, 255)

def setBattlefield():
    noStroke()
    for x in range(40):
        RedArr[x] = []
        GrnArr[x] = []
        BluArr[x] = []
        colorBattlefield(x)
setBattlefield()

def fight(x1, y1, x2, y2):
    if x2 >= 0 and x2 < 40 and y2 >= 0 and y2 < 40:
        if floor(random() * 3) + 1 == 1:
            RedArr[x1][y1] = RedArr[x2][y2]
            GrnArr[x1][y1] = GrnArr[x2][y2]
            BluArr[x1][y1] = BluArr[x2][y2]
        else:
            RedArr[x2][y2] = RedArr[x1][y1]
            GrnArr[x2][y2] = GrnArr[x1][y1]
            BluArr[x2][y2] = BluArr[x1][y1]

def setFights():
    xPos = 0
    yPos = 0
    for x in range(40):
        xPos = floor(random() * 40)
        for y in range(40):
            yPos = floor(random() * 40)
            fight(xPos, yPos, xPos - 1, yPos)
            fight(xPos, yPos, xPos + 1, yPos)
            fight(xPos, yPos, xPos, yPos - 1)
            fight(xPos, yPos, xPos, yPos + 1)

def drawBattlefield():
    for x in range(40):
        for y in range(40):
            fill(RedArr[x][y], GrnArr[x][y], BluArr[x][y])
            rect(x * 10, y * 10, 10, 10)

def draw():
    drawBattlefield()
    setFights()