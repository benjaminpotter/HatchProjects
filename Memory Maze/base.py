sizeOfBlocks = 50
arrayOfBlocks = []
chance = 5
charX = sizeOfBlocks / 2 - 2
charY = sizeOfBlocks / 2 - 2
charSize = sizeOfBlocks / 2
gameState = "Game"
start = millis()
timer = 0
countDown = 3
frameRate(15)

class Block:

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

def createBlocks():
    for y in range(0, 400, sizeOfBlocks):
        for x in range(0, 400, sizeOfBlocks):
            trial = round(random(0, chance))
            if trial == 1:
                arrayOfBlocks.push(Block(x, y, "bad"))
            else:
                arrayOfBlocks.push(Block(x, y, "safe"))
    arrayOfBlocks[0] = Block(0, 0, "start")
    arrayOfBlocks[len(arrayOfBlocks) - 1] = Block(400 - sizeOfBlocks, 400 - sizeOfBlocks, "end")
createBlocks()

def drawBlocks():
    for i in range(len(arrayOfBlocks)):
        if arrayOfBlocks[i].type == "safe":
            fill(255,255,255)
        if arrayOfBlocks[i].type == "bad":
            fill(255, 0, 0)
        if timer > countDown:
            fill(255, 255, 0)
        if arrayOfBlocks[i].type == "start" or arrayOfBlocks[i].type == "end":
            fill(0, 255, 0)
        rect(arrayOfBlocks[i].x, arrayOfBlocks[i].y, sizeOfBlocks, sizeOfBlocks)
        
def updateCharacter():
    fill(0)
    ellipse(charX, charY, charSize, charSize);
    if keyPressed and keyCode == RIGHT and charX < 400 - sizeOfBlocks:
        charX += sizeOfBlocks
    if keyPressed and keyCode == LEFT and charX > 0 + sizeOfBlocks:
        charX -= sizeOfBlocks
    if keyPressed and keyCode == UP and charY > 0 + sizeOfBlocks:
        charY -= sizeOfBlocks
    if keyPressed and keyCode == DOWN and charY < 400 - sizeOfBlocks:
        charY += sizeOfBlocks

def checkCollision():
    for i in range(len(arrayOfBlocks)):
        if dist(charX, charY, arrayOfBlocks[i].x, arrayOfBlocks[i].y) < sizeOfBlocks / 1.5:
            if arrayOfBlocks[i].type == "bad":
                gameState = "Game Over"
            if arrayOfBlocks[i].type == "end":
                gameState = "Win"
        
def timerCount():
    timer = (millis() - start) / 1000

def draw():
    if gameState == "Game Over":
        background(255, 0, 0)
    elif gameState == "Win":
        background(0, 255, 0)
    else:
        drawBlocks()
        updateCharacter()
        checkCollision()
        timerCount()