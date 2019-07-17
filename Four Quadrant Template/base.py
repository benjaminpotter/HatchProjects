count = 0
def drawAxis():
  background(255, 255, 255)
  fill(143, 143, 143)
  line(200, 20, 200, 355)
  line(45, 200, 370, 200)

drawAxis()
def drawAxisLabels():
  for j in range (50, 400, 50) :
    line(j, 210, j, 200),
    text(count - 15, j - 5, 225)
    line(200, j, 190, j)
    text(count - 15, 175, 400-j+5)
    count += 5

drawAxisLabels()
