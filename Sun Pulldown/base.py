r = 0
g = 0
b = 0
def colorFade():
  r = map(mouseY,400,0,0,103)
  g = map(mouseY,400,0,0,207)
  b = map(mouseY,400,0,0,247)
  background(r,g,b)

def drawSun():
  fill(224,180,20)
  noStroke()
  ellipse(200,mouseY+300,600,600)

def draw():
  colorFade()
  drawSun()
