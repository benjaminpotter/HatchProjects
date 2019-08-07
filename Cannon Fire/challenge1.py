x = 100
var y = 0
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

def fireCannonBall():
   x += 10
   y = 400 - (((-1 / 279) * Math.pow((x - 231), 2)) + 235)
   fill(0, 0, 0)
   imageMode(CENTER)
   image(getImage("avatars/mr-pink-green"), x, y, 40, 40)
   if x > 365 :
       x = 365
       
def draw():
   background(235, 241, 255)
   fireCannonBall()
   drawCannon()
