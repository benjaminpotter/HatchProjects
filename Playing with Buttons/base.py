buttonPosition = [160,160]
buttonColor = [100, 100, 100]
def drawButton():
  background(0, 0, 0)
  fill(buttonColor[0], buttonColor[1], buttonColor[2])
  rect(buttonPosition[0], buttonPosition[1], 80, 40)
  fill(255, 255, 255)
  text("Click Me!", buttonPosition[0] + 15, buttonPosition[1] + 25)

def randomizeButton():
  if mouseX > buttonPosition[0] and mouseX < buttonPosition[0] + 80 and mouseY > buttonPosition[1] and mouseY < buttonPosition[1] + 40 :
    buttonPosition = [random(5, 355), random(5, 355)]
    buttonColor = [random(0,255), random(0,255), random(0,255)]

def draw():
  drawButton()

def mouseClicked():
  randomizeButton()
