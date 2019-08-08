def drawBackground():
   noStroke()
   background(125, 255, 255)
   fill(68, 255, 0)
   rect(0, 200, 400, 200)

def drawCar():
   fill(0, 0, 255)
   rect(200, 190, 40, 10)
   rect(210, 180, 20, 10)
   fill(0, 0, 0)
   ellipse(210, 200, 10, 10)
   ellipse(230, 200, 10, 10)
   
def draw():
   drawBackground()
   drawCar()
