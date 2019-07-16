def drawHockeyRink() :
  background(255, 255, 255)
  noFill()
  stroke(255, 0, 0)
  arc(200, 170, 250, 100, 0, 360)
  line(0, 170, 400, 170)
  stroke(0, 0, 255)
  line(0, 50, 400, 50)
  line(0, 350, 400, 350)

def drawPuck() :
  fill(0)
  noStroke()
  ellipse(mouseX, mouseY, mouseY / 3, mouseY / 6)

def draw() :
  drawHockeyRink()
  drawPuck()
