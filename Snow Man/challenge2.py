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

def drawHat():
   fill(0, 0, 0)
   noStroke()
   rect(150, 70, 100, 20)
   rect(160, 25, 80, 50)

def drawScarf():
   fill(240, 10, 0)
   rect(140, 151, 120, 25)

def draw():
   translate(100, 0)
   drawSnowman()
   drawHat()
   drawScarf()
   resetMatrix()
   translate(-100, 0)
   drawSnowman()
   drawHat();
   drawScarf()
