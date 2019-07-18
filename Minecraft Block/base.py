arrayOfBlocks = []

class Block:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.numHits = 1
        
def createBlocks():
    for i in range(8):
        for j in range(8):
            arrayOfBlocks.append(Block(i * 50, j * 50))
createBlocks()

def hitBlock():
    for block in arrayOfBlocks:
        if mouseX > block.x and mouseX < block.x + 50 and mouseY > block.y and mouseY < block.y + 50:
            if block.numHits < 3:
                block.numHits += 1
            else:
                block.numHits = 0

def drawBricks():
    for block in arrayOfBlocks:
        if block.numHits > 0 and block.numHits < 4:
            fill(125, 69, 0)
            rect(block.x, block.y, 50, 50)

def drawCracks(var1, var2, var3, var4, var5, var6, var7, var8, timesHit):
    for block in arrayOfBlocks:
        if block.numHits > timesHit:
            line(block.x + var1, block.y + var2,
                 block.x + var3, block.y + var4)
            line(block.x + var5, block.y + var6,
                 block.x + var7, block.y + var8)

def mouseClicked(e):
    hitBlock()

def draw():
    background(255)
    strokeWeight(5)
    drawBricks()
    drawCracks(20, 36, 18, 17, 30, 32, 40, 16, 1)
    drawCracks(10, 25, 34, 19, 10, 38, 37, 40, 2)