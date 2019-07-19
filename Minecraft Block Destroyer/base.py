blockSize = 20
arrayOfBlocks = {
  "color" : [],
  "type" : [],
  "posX" : [],
  "posY" : []
}
numGrass = 0
numIron = 0
numDirt = 0
grassBlock = {
  "blockType" : "grass",
  "color" : color(0, 255, 0),
  "maxHeight" : 240,
  "minHeight" : 260,
    "rarity" : 1
}
dirtBlock = {
  "blockType" : "dirt",
  "color" : color(138, 51, 11),
  "maxHeight" : 240,
  "minHeight" : 400,
    "rarity" : 0
}
ironBlock = {
  "blockType" : "iron",
  "color" : color(102, 102, 102),
  "maxHeight" : 280,
  "minHeight" : 380,
  "rarity" : 8
}
def addBlock(x, y, c, t):
  arrayOfBlocks[posX].append(x)
  arrayOfBlocks[posY].append(y)
  arrayOfBlocks[color].append(c)
  arrayOfBlocks[type].append(t)

def getBlockAt(x, y):
  for i in range (0, len(arrayOfBlocks[posX])) :
    if dist(x, y, arrayOfBlocks[posX][i] + (blockSize/2), arrayOfBlocks[posY][i] + (blockSize/2)) < 10 :
      return i

  return False

def generateWorld(block):
    for i in range (400,0, -20):
        for j in range (400, 0, -20) :
            if j >= block[maxHeight] and j <= block[minHeight] and getBlockAt(i + (blockSize/2),j + (blockSize/2)) == False :
                if random(0,10) >= block[rarity] :
                    addBlock(i, j, block[color], block[blockType])

generateWorld(grassBlock)
generateWorld(ironBlock)
generateWorld(dirtBlock)
def drawBlocks() :
  for i in range (0, len(arrayOfBlocks[color])):
    fill(arrayOfBlocks[color][i])
    rect(arrayOfBlocks[posX][i], arrayOfBlocks[posY][i], blockSize, blockSize)

def drawInventory() :
  fill(grassBlock[color])
  rect(20, 20, 30, 30)
  fill(dirtBlock[color])
  rect(80, 20, 30, 30)
  fill(ironBlock[color])
  rect(140, 20, 30, 30)
  fill(255, 255, 255)
  textSize(20)
  textAlign(CENTER,CENTER)
  text(numGrass, 35, 38)
  text(numDirt, 95, 38)
  text(numIron, 150, 38)

def pickUpBlock(id) :
    if arrayOfBlocks[type][id] == "grass":
      numGrass+=1
    if arrayOfBlocks[type][id] == "dirt":
      numDirt+=1
    if arrayOfBlocks[type][id] == "iron":
      numIron+=1

def digBlock(id) :
  pickUpBlock(id)
  arrayOfBlocks[color].splice(id, 1)
  arrayOfBlocks[type].splice(id, 1)
  arrayOfBlocks[posX].splice(id, 1)
  arrayOfBlocks[posY].splice(id, 1)

def mouseClicked() :
  if getBlockAt(mouseX, mouseY) !=  False :
    digBlock(getBlockAt(mouseX, mouseY))

def draw() :
  background(0, 193, 207)
  drawBlocks()
  drawInventory()
