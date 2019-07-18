angleMode(DEGREES)

numOfHair = 100
xSpeed = 1
ySpeed = 1 
endPointX = 120
endPointY = 70

def drawEyes():
  fill(255)
  stroke(0)
  ellipse(-20,0,40,40)
  ellipse(20,0,40,40)
  noStroke()
  fill(25,246,185)
  ellipse(-20,0,20,20)
  ellipse(20,0,20,20)
def drawHair():
    translate(width/2,height/2)
    noFill()
    stroke(121,70,122)
    for i in range(0, numOfHair):
        rotate(360/numOfHair)
        bezier(0,50,0,60,80,80,endPointX,endPointY)
  
def animateHair():
    global animateHair
    if endPointY >= 130 or endPointY <= 60:
        ySpeed *= -1
    if endPointX >= 130 or endPointX <= 60:
        xSpeed *= -1
  
endPointY += ySpeed
endPointX += xSpeed

def draw():
  background(225,255,251)
  drawHair()
  drawEyes()
  animateHair()
