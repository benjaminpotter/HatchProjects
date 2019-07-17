blocksWide = 16
blocksDeep = 16
blocksTall = 256
answer = 0
def drawChunk():
  noFill()
  rect(180, 100, 16, 256)
  line(180,100,190,95)
  line(196,100,206,95)
  line(190,95,206,95)
  line(206,95,206,346)
  line(196,356,206,346)

def displayQuestion():
  fill(255, 0, 0)
  textSize(20)
  text("How many blocks are in a chunk?", 50, 50)

def calculateBlocks():
  answer = blocksWide * blocksTall * blocksDeep

def displayAnswer():
  if keyIsPressed :
    textSize(10)
    text(blocksWide, 182, 370)
    text(blocksDeep, 200, 360)
    text(blocksTall, 214, 199)
    textSize(25)
    text(answer + " Blocks", 120, 80)

def draw():
  background(238, 255, 0)
  drawChunk()
  displayQuestion()
  calculateBlocks()
  displayAnswer()
