trailX = []
trailY = []

def drawRink() :
  background(255, 255, 255)
  fill(255, 0, 0)
  rect(0,190,400,20)
  ellipse(200,200,80,80)
  fill(86, 174, 237)
  rect(0,45,400,10)
  rect(0,355,400,10)

def addSkatePosition() :
  trailX.push(mouseX)
  trailY.push(mouseY)

def drawTrail() :
  noFill()
  stroke(82, 82, 82, 80)
  for j in range (0, 2) :
    beginShape()
    for i in range (0, trailX.length, 5) :
      curveVertex(trailX[i] + j * 5, trailY[i] + j * 5)
    endShape()

def draw() :
  drawRink()
  addSkatePosition()
  drawTrail()
