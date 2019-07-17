flap = 0
flapSpeed = 8
noStroke()
def drawBody():
  fill(0)
  translate(mouseX,mouseY)
  ellipse(0,0,30,30)
  triangle(-10,0,10,0,0,20)
  triangle(-10,0,0,0,-5,-20)
  triangle(10,0,0,0,5,-20)

def drawWings():
  rotate(flap)
  flap += flapSpeed
  if flap > 30 or flap < -30 :
    flapSpeed = -flapSpeed
  triangle(0,0,40,-20,60,10)
  resetMatrix()
  translate(mouseX,mouseY)
  rotate(-flap)
  triangle(0,0,-40,-20,-60,10)
  resetMatrix()

def drawEyes() :
  fill(255)
  ellipse(mouseX-5,mouseY-5,3,5)
  ellipse(mouseX+5,mouseY-5,3,5)

def draw():
  background(249,148,16)
  drawBody()
  drawWings()
  drawEyes()
