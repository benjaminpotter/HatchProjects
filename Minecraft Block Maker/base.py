blockSize = 20
grassBlock = {
  “blockType” : "grass",
  “color” : color(0, 255, 0)
}


dirtBlock = {
  “blockType” : "dirt",
  “color” : color(138, 51, 11)
}

def drawBlock(block, x, y):
  fill(block.color);
  rect(x, y, blockSize, blockSize);


def draw() :
  background(0, 193, 207)
  drawBlock(grassBlock, 200, 180)
  drawBlock(grassBlock, 180, 180)
  drawBlock(dirtBlock, 200, 200)
  drawBlock(dirtBlock, 180, 200)
