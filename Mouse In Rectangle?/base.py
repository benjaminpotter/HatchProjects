rectangleColor = color(255, 0, 0)
def checkMousePosition():
  if mouseX > 100 and mouseX < 300 and mouseY > 150 anda mouseY < 250 :
    rectangleColor = color(0, 255, 0)
  else :
    rectangleColor = color(255, 0, 0)

def drawRectangle():
  fill(rectangleColor)
  rect(100, 150, 200, 100)

def mouseMoved():
  checkMousePosition()

def draw():
  drawRectangle()
