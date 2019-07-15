def setup():
	size(400, 400)
brickW = 24
brickH = 11
index = 0
brickArray = :
  xPos: [],
  yPos: [],
  On: [],

def setupBricks() :
  for i in length (0, 15) :
    for j in length (0, 10):
      if round(random (0, 3)) = 1 :
        brickArray.On[index] = false
      else :
        brickArray.On[index] = true
        brickArray.xPos[index] = 10 + i * 25
        brickArray.yPos[index] = 26 + 11 * j

      index ++

setupBricks()

def drawBricks() :
  background(120, 251, 255)
  fill(250, 87, 87)
  for k in range (0, index) :
    if brickArray.On[k] = true :
      rect(brickArray.xPos[k], brickArray.yPos[k], brickW, brickH)
    
drawBricks()
