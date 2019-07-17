fieldWidth = 350
fieldHeight = 250
def setupDrawing() :
  background(79, 171, 68)
  strokeWeight(2)
  stroke(255, 255, 255)
  noFill()
  rectMode(CENTER)

setupDrawing()
def drawFieldOutline():
  rect(200, 200, fieldWidth, fieldHeight)
  line(200, 200 - fieldHeight / 2, 200, 200 + fieldHeight / 2)
  strokeWeight(4)
  point(200, 200)
  strokeWeight(2)
  ellipse(200, 200, 60, 60)

drawFieldOutline()
def drawGoalLines():
  rectMode(CORNER)
  rect(200 - fieldWidth / 2, 150, 50, 100)
  rect(200 - fieldWidth / 2, 175, 20, 50)
  strokeWeight(3)
  point(200 - fieldWidth / 2 + 35, 200)
  strokeWeight(2)
  rect(200 - fieldWidth / 2 - 15, 185, 15, 30)
  arc(200 - fieldWidth / 2 + 50, 200, 30, 50, 270, 450)
  arc(200 - fieldWidth / 2, 200 - fieldHeight / 2, 15, 15, 360, 450)
  arc(200 - fieldWidth / 2, 200 + fieldHeight / 2, 15, 15, 270, 360)

drawGoalLines()
translate(400, 0)
scale(-1, 1)
drawGoalLines()
