def drawShapes():
  fill(0,0,0)
  ellipse(0,0,20,20)
  noFill()
  rect(0,0,200,200)

def draw():
  background(181, 215, 224)
  drawShapes()

def mouseClicked():
  translate(50,50)

def keyPressed():
  if keyCode == RIGHT :
    rotate(-45)

  if keyCode == LEFT :
    rotate(45)

  if keyCode == UP :
    scale(1.5)

  if keyCode == DOWN :
    scale(0.5)

  if key === ' ' :
    resetMatrix()
