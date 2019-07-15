def setup():
	size(400, 400)
xW = 0
yW = 0
x = 0
y = 0
n = 0

stroke(80, 175, 0)
strokeWeight(3)

def updatePos() :
  r = random(100)
  if r <= 1 :
    xW = 0
    yW = 0.16 * y
  elif (r <= 8) :
    xW = 0.2 * x - 0.26 * y;
    yW = 0.23 * x + 0.22 * y + 1.6;
  elif (r <= 15) :
    xW = -0.15 * x + 0.28 * y;
    yW = 0.26 * x + 0.24 * y + 0.44;
  elif
    xW = 0.85 * x + 0.04 * y;
    yW = -0.04 * x + 0.85 * y + 1.6;
 
  x = xW
  y = yW

def drawFern():
  for i in range (0, 5000) :
    updatePos()
    point(x * 35 + 200,-y * 35 + 410)
  x = 0
  y = 0

background(100)
drawFern()
