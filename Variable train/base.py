xPos = 140
yPos = 245
noStroke()

def drawTrainHead() :
  fill(225, 66, 67)
  rect(xPos, yPos, 45, 100)
  rect(xPos - 90, yPos + 30, 110, 70, 20)
  rect(xPos - 70, yPos + 10, 20, 20)
  fill(0)
  rect(xPos - 75, yPos + 5, 30, 10, 5)
  ellipse(xPos + 15, yPos + 105, 50, 50)
  ellipse(xPos - 65, yPos + 110, 30, 30)
  ellipse(xPos - 30, yPos + 110, 30, 30)
  fill(255)
  rect(xPos + 5, yPos + 5, 35, 25)

def draw() :
  background(255)
  drawTrainHead()
