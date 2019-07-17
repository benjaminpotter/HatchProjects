blackC = color(0, 0, 0)
darkC = color(80, 80, 80)
lightC = color(180, 180, 180)
whiteC = color(255, 255, 255)
cells = 15
cellSize = 400 / cells
halfCell = cellSize / 2
d2 = cellSize * 0.85
d1 = cellSize * 0.7
def drawCircle(x, y, theta) :
  fill(blackC)
  var theta1 = theta + 180
  var theta2 = theta + 360
  arc(x, y, d2, d2, theta1, theta2)
  fill(whiteC)
  arc(x, y, d2, d2, theta, theta1)
  fill(darkC)
  ellipse(x, y, d1, d1)
noStroke()
background(lightC)
for i in range (0, cells) :
    x = i * cellSize
    for j in range (0, cells) :
        y = j * cellSize
        drawCircle(x + halfCell, y + halfCell, (i - j) * 45)
