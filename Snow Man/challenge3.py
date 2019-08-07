yPos = 10
ySpeed = 2
def drawBackground():
   background(204, 234, 252)
   fill(255, 255, 255)
   noStroke()
   ellipse(100, 400, 300, 200)
   ellipse(300, 400, 400, 150)
drawBackground()

def drawSnowman():
   stroke(100)
   ellipse(200, 300, 150, 150)
   ellipse(200, 200, 125, 125)
   ellipse(200, 125, 100, 100)
   fill(255, 131, 0)
   ellipse(186, 105, 10, 10)
   ellipse(216, 105, 10, 10)
   fill(255, 131, 0)
   triangle(200, 125, 200, 140, 230, 130)
drawSnowman()

def drawSnow():
   fill(255, 255, 255)
   ellipse(20, yPos, 10, 10)
   ellipse(50, yPos + 15, 10, 10)
   ellipse(100, yPos + 50, 10, 10)
   ellipse(120, yPos, 10, 10)
   ellipse(160, yPos + 5, 10, 10)
   ellipse(200, yPos + 100, 10, 10)
   ellipse(220, yPos + 12, 10, 10)
   ellipse(250, yPos + 50, 10, 10)
   ellipse(280, yPos + 20, 10, 10)
   ellipse(320, yPos + 10, 10, 10)
   ellipse(350, yPos + 50, 10, 10)
   ellipse(370, yPos, 10, 10)
   yPos = yPos + ySpeed
   if yPos > 400 :
       yPos = 0

def draw():
   drawBackground()
   drawSnowman()
   drawSnow()
