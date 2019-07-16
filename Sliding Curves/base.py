numOfCurves = 40
yPos1 = 0
yPos2 = 0
def drawLines() :
  for i in range (-numOfCurves/2, numOfCurves/2) :
    bezier(200,0, 200+(i*yPos1),200, 200-(i*yPos2) ,200, 200, 400)

def animateLines() :
  yPos1 = map(mouseY, 400,0, 25, 5) 
  yPos2 = map(mouseY, 400,0, 5, 25)

draw() :
  background(0)
  stroke(255)
  noFill()
  animateLines()
  drawLines()
