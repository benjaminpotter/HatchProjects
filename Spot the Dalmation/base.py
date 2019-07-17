def drawCollar() :
  noStroke()
  fill(0, 196, 230)
  rect(0, 155, 400, 30)
  fill(255, 242, 0)
  quad(200, 175, 160, 225, 200, 275, 240, 225)

drawCollar()

def drawDot() :
  fill(0, 0, 0)
  var dotSize = random(15,50)
  ellipse(mouseX, mouseY, dotSize, dotSize)

def mouseClicked() :
  drawDot()
  drawCollar()
