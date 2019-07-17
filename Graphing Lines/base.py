x = 0
y = 0
def drawingSetup():
  background(255, 255, 255)
  fill(143, 143, 143)
  stroke(222, 222, 222)

drawingSetup()
def drawGraph():
  for j in range (50, 400, 50) :
    line(j, 374, j, 0)
    text(j, j, 395)
    line(400, j, 30, j)
    text(400-j, 4, j+3)

drawGraph()
def drawPoint():
  x++
  y = x
  fill(0, 153, 255)
  ellipse(x,400-y, 5, 5)

def draw():
  noStroke()
  drawPoint()
