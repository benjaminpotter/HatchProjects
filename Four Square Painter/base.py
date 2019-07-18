def fourSquareOutLine():
  line(200, 0, 200, 400)
  line(0, 200, 400, 200)

def setRandomColour():
  fill(random(0, 255), random(0, 255), random(0, 255));

def drawSquare():
  if (mouseX < 200 and mouseY < 200): 
    rect(0, 0, 200, 200)
  elif (mouseX < 200 and mouseY > 200):
    rect(0, 200, 200, 200)
  elif (mouseX > 200 and mouseY < 200): 
    rect(200, 0, 200, 200)
  elif (mouseX > 200 and mouseY > 200): 
    rect(200, 200, 200, 200)
  
def mouseClicked(e):
  setRandomColour()
  drawSquare()
  fourSquareOutline()
