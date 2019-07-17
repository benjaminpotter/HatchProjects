angle = 0
x = 0
y = 0
noStroke()
def setPoints():
  xMax = 0
  xMin = 400
  yMax = 0
  yMin = 400
  numOfPoints = random(10,30)
  size = random(300,800)
  distPerPoint = size/numOfPoints
  degPerPoint = 360/numOfPoints

  for i in range (0, numOfPoints):
    moveAngle = angle+random(-angle,angle)
    x += cos(moveAngle)*distPerPoint
    y += sin(moveAngle)*distPerPoint
    curveVertex(x, y)
    angle += degPerPoint
    if x > xMax :
      xMax = round(x)
    if x < xMin :
      xMin = round(x)
    if y > yMax :
      yMax = round(y)
    if y < yMin :
      yMin = round(y)

def randomSplash(xStart,yStart):
  x = xStart
  y = yStart
  beginShape()
  curveVertex(x,y)
  setPoints()
 
  curveVertex(xStart,yStart)
  endShape()

def mouseClicker:()
  fill(random(50,255),random(50,255),random(50,255),random(50,100))
  randomSplash(mouseX,mouseY)
