def setup():
	size(400, 400)
def drawStamp() :
  strokeWeight(4)
  fill(255, 255, 0)
  ellipse(mouseX, mouseY, 100, 100)
  fill(0)
  ellipse(mouseX - 20, mouseY - 10, 15, 15)
  ellipse(mouseX + 20, mouseY - 10, 15, 15)
  noFill()
  arc(mouseX, mouseY + 20, 30, 30, 0, 3)

background(20)
def mouseClicked() :
  drawStamp()
