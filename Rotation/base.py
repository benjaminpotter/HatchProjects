def drawShapes():
  fill(0,0,0)
  ellipse(100,100,20,20)
  fill(255,0,0)
  ellipse(100,-100,20,20)
  fill(0,255,0)
  ellipse(-100,-100,20,20)
  fill(0,0,255)
  ellipse(-100,100,20,20)
  noFill()
  rect(0,0,400,400)

def draw() :
  background(181, 215, 224) 
  drawShapes()

def mouseClicked() :
  rotate(15)
