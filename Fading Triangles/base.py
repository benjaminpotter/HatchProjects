points = []
colorRed=0
colorGreen=0
colorBlue=0
r = random(0,255)
g= random(0,255)
b= random(0,255)
counter=0
frame = 500
background(0, 0, 0)
def position(x,y) :
  this.x = x
  this.y = y
  this.xSpeed = random(-2,2)
  this.ySpeed = random(-2,2)

points.append(new position(0,0))
points.append(new position(0,400))
points.append(new position(200,400))
def wallCollision() :
  for i in range (0, points.length):
    if points[i].x>400 or points[i].x<0 :
      points[i].xSpeed=-points[i].xSpeed

    if points[i].y>400 or points[i].y<0 :
      points[i].ySpeed=-points[i].ySpeed

def updateColor() :
  if counter > frame :
    r2= random(-100,355)
    g2= random(-100,355)
    b2= random(-100,355)
    colorRed=(r2-r)/frame
    colorGreen=(g2-g)/frame
    colorBlue=(b2-b)/frame
    r2=r
    g2=g
    b2=b
    counter=0
  r+=colorRed
  g+=colorGreen
  b+=colorBlue
  counter+=1

def drawTriangle() :
  strokeWeight(0.03)
  stroke(r, g, b)
  noFill()
  triangle(points[0].x, points[0].y, points[1].x, points[1].y, points[2].x,   points[2].y)

def updateTriangle() :
  for i in range (0, points.length):
    points[i].x+=points[i].xSpeed
    points[i].y+=points[i].ySpeed


def draw() :
  frameRate(100)
  wallCollision()
  updateColor()
  updateTriangle()
  drawTriangle()
