atLeastOneCircle = FALSE
lastX = 0
lastY = 0
def recordLastLocation():
  lastX = mouseX
  lastY = mouseY

def drawCircle():
  var size = random(10, 50)
  fill(random(0, 255), random(0, 255), random(0, 255))
  ellipse(mouseX, mouseY, size, size)
  recordLastLocation()
  atLeastOneCircle = true

def drawLine():
  strokeWeight(random(1, 5))
  stroke(random(0, 255), random(0, 255), random(0, 255))
  line(lastX, lastY, mouseX, mouseY)

def mouseClicked():
  if atLeastOneCircle == TRUE :
    drawLine()
    drawCircle()
  else :
    drawCircle()
