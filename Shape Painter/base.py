xPoints = []
yPoints = []
def drawShape() :
  fill(random(50,255), random(50,255), random(50,255))
  beginShape()
  for i in range (0, xPoints.length) :
    vertex(xPoints[i], yPoints[i])
  endShape(CLOSE)

def clearPoints() :
  xPoints = []
  yPoints = []

def drawPoints() :
  stroke(0, 0, 0)
  strokeWeight(5)
  xPoints.push(mouseX)
  yPoints.push(mouseY)
  point(mouseX, mouseY)

def mouseClicked() :
  if dist(mouseX, mouseY, xPoints[0], yPoints[0]) < 20 :
    drawShape()
    clearPoints()
  else :
    drawPoints()
