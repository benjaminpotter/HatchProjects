fuzzy = getImage("avatars/mr-pink")
grassyKnoll = getImage("cute/GrassBlock")
def drawScene():
  scale(4, 4)
  image(grassyKnoll, 0, -54)
  resetMatrix()
  scale(0.6, 0.6)
  image(fuzzy, 280, 240)
  resetMatrix()

def drawInnerStrokes():
  strokeWeight(4)
  noFill()
  for i in range (0, 100):
    stroke(0, 0, 0, 60 + i)
    ellipse(mouseX, mouseY, 80 + i * 3, 80 + i * 3)

def drawOuterStroke() :
  stroke(0, 0, 0)
  strokeWeight(400)
  ellipse(mouseX, mouseY, 775, 775)

def draw():
  drawScene()
  drawInnerStrokes()
  drawOuterStroke()
