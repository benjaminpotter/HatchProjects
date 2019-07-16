teal = color(7,135,131)
raspberry = color(175,45,102)
mint = color(60,255,170)
purple = color(68,31,79)
def displayColor ():
  fill(0)
  rect(0,100,400,10)
  fill(teal)
  rect(0,0,100,100)
  fill(raspberry)
  rect(100,0,100,100)
  fill(mint)
  rect(200,0,100,100)
  fill(purple)
  rect(300,0,100,100)

def selectColor():
  if mouseY<100 :
    if mouseX > 0 && mouseX < 100 :
      fill(teal)
    ifmouseX > 100 && mouseX < 200 :
      fill(raspberry)
    ifmouseX > 200 && mouseX < 300 :
      fill(mint)
    if mouseX > 300 && mouseX < 400 :
      fill(purple)

def drawGlob():
  if mousePressed :
    var size = random (0,50)
    var x = random(0,400)
    var y = random(110,400)
    selectColor()
    ellipse(x, y, size, size)

def draw():
  noStroke()
  drawGlob()
  displayColor()
