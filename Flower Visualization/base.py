data = [3,2.5,3,3.7,3,2,3,4]
numOfPetals = data.length
multiply = 3.7
var petalMultiply = 10
def drawSetup() :
  background(153, 196, 196)
  noStroke()
  translate(width/2, height/2)
  scale(multiply,multiply)
  ellipseMode(CORNERS)

drawSetup()
def drawPetal(i) :
  fill(random(0,255), 19, 100)
  ellipse(-3, 0, 3, data[i]*petalMultiply)

def drawFlower() :
  for i in range (0, numOfPetals) :
    rotate(360/numOfPetals)
    drawPetal(i)

drawFlower()

def drawCenter() :
  fill(255, 255, 46)
  ellipse(-7, -7, 7, 7)

drawCenter()
