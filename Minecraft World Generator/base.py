class Block:
    
    blockSize = 20
    
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        
        self.type = type
        
    def drawBlock(self):
        fill(self.type.color)
        rect(self.x, self.y, Block.blockSize, Block.blockSize)
        
    def generateBlock(x, y):
        if y >= grassBlock.maxHeight and y <= grassBlock.minHeight:
            addBlock(Block(x, y, grassBlock))
        elif y <= dirtBlock.minHeight and y >= dirtBlock.maxHeight:
            addBlock(Block(x, y, dirtBlock)) 
   
class BlockType:
    def __init__(self, color, maxHeight, minHeight):
        self.color = color
        self.maxHeight = maxHeight
        self.minHeight = minHeight
        
grassBlock = BlockType(color(0, 255, 0), 240, 240)
dirtBlock = BlockType(color(138, 51, 11), 240, 400)

blocks = []
def addBlock(block):
    blocks.append(block)
    
def generateWorld():
    for x in range(0, 400, Block.blockSize):
        for y in range(0, 400, Block.blockSize):
            Block.generateBlock(x, y)
            print('generated block')
            
generateWorld()

def drawBlocks():
    for block in blocks:
        block.drawBlock()
        print('drawn block') 

def draw():
    background(0, 193, 207)
    drawBlocks()