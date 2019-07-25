noStroke()
def drawBody():
   fill(132, 82, 44)
   rect(100, 123, 200, 200)
   arc(200, 125, 200, 200, 180, 360)
   image(getImage("cute/GrassBlock"), 0, 200, 400, 177)

drawBody()

def drawFace():
   fill(204, 33, 81)
   ellipse(200, 152, 75, 50)
   fill(0, 0, 0)
   ellipse(165, 90, 10, 58)
   ellipse(235, 90, 10, 58)
   fill(194, 184, 184)
   ellipse(165, 70, 6, 13)
   ellipse(235, 70, 6, 13)
   ellipse(188, 143, 33, 24)

drawFace()

def drawHair():
   stroke(255, 255, 80)
   strokeWeight(8)
   line(200, 22, 240, 12)
   line(200, 21, 200, 5)
   line(200, 22, 185, 8)
drawHair()
