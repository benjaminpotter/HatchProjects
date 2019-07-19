# NEEDS EDITING!!!

numGrass = 0
numIron = 0
numDirt = 0
blockSelected = "none"

inventory = [] 

class BlockType:
    def __init__(self, color, maxHeight, minHeight, rarity):
        self.color = color
        self.maxHeight = maxHeight
        self.minHeight = minHeight
        self.rarity = rarity
        
grassBlock = BlockType(color(0, 255, 0), 240, 260, 1)
dirtBlock = BlockType(color(138, 51, 11), 240, 400, 0)
ironBlock = BlockType(color(102, 102, 102), 280, 380, 8)

class Block:
    
    blockSize = 20
    
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        
        self.type = type
        
    def drawBlock(self):
        fill(self.type.color)
        rect(self.x, self.y, Block.blockSize, Block.blockSize)
        
blocks = []
def addBlock(block):
    blocks.append(block)

def getBlockAt(x, y):
    
    x_adj = floor(x / Block.blockSize) * Block.blockSize
    y_adj = floor(y / Block.blockSize) * Block.blockSize
    
    for block in blocks:
        if block.x == x and block.y == y:
            return block
    return None

def generateWorld(blockType):
    for x in range(0, 400, Block.blockSize):
        for y in range(0, 400, Block.blockSize): 
            if x >= blockType.maxHeight and y <= blockType.minHeight and getBlockAt(x + (Block.blockSize/2), y + (Block.blockSize/2)) == False:
                if random(0,10) >= blockType.rarity:
                    addBlock(Block(x, y, blockType))  

generateWorld(grassBlock)
generateWorld(ironBlock)
generateWorld(dirtBlock)

def drawBlocks():
    for block in blocks:
        block.drawBlock()
  
def drawInventory():
    fill(grassBlock.color)
    rect(20, 20, 30, 30)
    fill(dirtBlock.color)
    rect(80, 20, 30, 30)
    fill(ironBlock.color)
    rect(140, 20, 30, 30)
    fill(255, 255, 255)
    textSize(20)
    textAlign(CENTER,CENTER)
    text(numGrass, 35, 38)
    text(numDirt, 95, 38)
    text(numIron, 150, 38)

def pickUpBlock(block):
    type(block)
    #inventory.append(block.type)
  
def digBlock(block):
    pickUpBlock(block)
    
    blocks.remove(block)

def clickInventory():
    if mouseX > 20 and mouseX < 50 and mouseY > 20 and mouseY < 50:
        blockSelected = "Grass"
    elif mouseX > 80 and mouseX < 110 and mouseY > 20 and mouseY < 50:
        blockSelected = "Dirt"
    elif mouseX > 140 and mouseX < 190 and mouseY > 20 and mouseY < 50:
        blockSelected = "Iron"

def displaySelectedBlock():
    noFill()
    strokeWeight(5)
    stroke(255)
    
    if blockSelected == 'Grass':
        rect(20, 20, 30, 30)
    if blockSelected == 'Dirt':
        rect(80, 20, 30, 30)
    if blockSelected == 'Iron': 
      rect(140, 20, 30, 30)

def removeItem(blockType):
    if blockType in inventory:
        inventory.remove(blockType)

def createBlock(blockType):
    roundedX = floor(mouseX/ Block.blockSize) * Block.blockSize
    roundedY = floor(mouseY/Block.blockSize) * Block.blockSize
    
    removeItem(blockType)
    addBlock(Block(roundedX, roundedY, blockType))

def mouseClicked(e):
    block = getBlockAt(mouseX, mouseY)
    if block != None:
        digBlock(block)
    elif mouseY < 100:
        clickInventory()
    else:
        createBlock(toBlockType())

def toBlockType():
    if blockSelected == 'Grass':
        return grassBlock
    if blockSelected == 'Dirt':
        return dirtBlock
    if blockSelected == 'Iron': 
        return Iron

def draw():
    background(0, 193, 207)
    drawBlocks()
    drawInventory()
    displaySelectedBlock()
