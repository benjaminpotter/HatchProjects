def drawCentreCircles():
  fill(255, 149, 36)
  noStroke()
  ellipse(120, 200, 40, 40)
  ellipse(320, 200, 40, 40)

drawCentreCircles()
def drawBigCircles():
  fill(65, 155, 252)
  for i in range (0, 6):
    resetMatrix()
    translate(120,200)
    rotate(i * 60)
    ellipse(0, -80, 70, 70)

drawBigCircles()
def drawSmallCircles():
  for i in range (0, 8):
    resetMatrix()
    translate(320,200)
    rotate(i * 45)
    ellipse(0, -35, 20, 20)

drawSmallCircles()
