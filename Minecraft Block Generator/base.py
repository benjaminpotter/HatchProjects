blockSize = 20
arrayOfBlocks = {'color': [], 'type': [], 'posX': [], 'posY': []}
grassBlock = {'blockType': "grass", 'color': color(0, 255, 0), 'maxHeight': 240, 'minHeight': 240}
dirtBlock = {'blockType': "dirt", 'color': color(138, 51, 11), 'maxHeight': 240, 'minHeight': 400}

def addBlock(x, y, c, t):
    arrayOfBlocks['posX'].append(x)
    arrayOfBlocks['posY'].append(y)
    arrayOfBlocks['color'].append(c)
    arrayOfBlocks['type'].append(t)

def generateBlock(block):
    for i in range(400, 0, -20):
        for j in range(400, 0, -20):
            if j >= block['maxHeight'] and j <= block['minHeight']:
                addBlock(i, j, block['color'], block['blockType'])

generateBlock(dirtBlock)
generateBlock(grassBlock)

def drawBlocks():
    for i in range(len(arrayOfBlocks['color'])):
        fill(arrayOfBlocks['color'][i])
        rect(arrayOfBlocks['posX'][i], arrayOfBlocks['posY'][i], blockSize, blockSize)

def draw():
    background(0, 193, 207)
    drawBlocks()
