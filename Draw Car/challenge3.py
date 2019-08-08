def drawBackground():
   noStroke()
   background(125, 255, 255)
   fill(68, 255, 0)
   rect(0, 200, 400, 200)

def drawMotorcycle():
   fill(255, 0, 0)
   arc(210, 200, 15, 15, 180, 360)
   arc(230, 200, 15, 15, 180, 360)
   rect(206, 190, 27, 7)
   stroke(255, 0, 0)
   strokeWeight(3)
   line(233, 190, 235, 181)
   line(235, 181, 230, 181)
   noStroke()
   fill(119, 119, 119)
   arc(220, 190, 18, 10, 180, 360)
   fill(0, 0, 0)
   ellipse(210, 200, 10, 10)
   ellipse(230, 200, 10, 10)

def draw():
   drawBackground()
   drawMotorcycle()
