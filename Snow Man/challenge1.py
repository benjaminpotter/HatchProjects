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

def drawArms():
   stroke(210, 105, 30)
   line(262, 200, 300, 160)
   line(137, 200, 99, 160)
drawArms();

def drawButtons():
   fill(0, 0, 0)
   noStroke()
   ellipse(200, 190, 10, 10)
   ellipse(200, 210, 10, 10)
   ellipse(200, 230, 10, 10)

drawButtons()

def drawHat():
   rect(150, 70, 100, 20)
   rect(160, 25, 80, 50)

drawHat()
