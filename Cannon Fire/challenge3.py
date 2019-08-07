x1 = 100
y1 = 0
x2 = 275
y2 = 130
noStroke()

def drawCannon():
   fill(230, 225, 230)
   rect(0, 256, 400, 150)
   fill(87)
   translate(76, 219)
   rotate(161)
   ellipse(0, 0, 139, 79)
   quad(-33, 35, -75, 24, -78, -17, -47, -29)
   resetMatrix()
   fill(170)
   ellipse(60, 250, 70, 70)


var drawcollision():
   x1 += 10
   y1 = 400 - (((-1 / 279) * Math.pow((x1 - 231), 2)) + 235)
   fill(0, 0, 0)
   ellipse(x1, y1, 40, 40)
   if x1 > 365 :
       x1 = 365
   fill(139,69,19)
   rect(x2, y2, 30, 230)
   if x1 > 274 :
       x2 += 10
       y2 = 400 - (((-1 / 279) * Math.pow((x1 - 231), 2)) + 235)
       rect(274, 230, 230, 30)


def draw():
   background(235, 241, 255);
   drawcollision()
   drawCannon()
