circleSize = 400
speed = 5

def drawCircle():
  ellipse(200,200, circleSize, circleSize)
  circleSize -= speed

def draw():
  noStroke()
  fill(179,155,123)
  background(50,83,102)
  drawCircle()

def mouseClicked():
  circleSize = 400
