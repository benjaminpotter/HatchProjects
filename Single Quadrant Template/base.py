count = 0
def drawAxis():
  background(255, 255, 255)
  fill(143, 143, 143)
  line(50, 20, 50, 355)
  line(45, 350, 370, 350)

drawAxis()
def drawAxisLabels():
  for j in range (50, 400, 50) :
    line(j, 350, j, 355)
    text(count, j - 3, 370)
    line(50, j, 45, j)
    text(count, 28, 400-j+5)
    count += 5

drawAxisLabels()
