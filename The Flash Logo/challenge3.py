def drawBackground():
   fill(222, 36, 36)
   noStroke()
   rect(0, 40, 400, 250, 60)
   stroke(0, 0, 0)
   strokeWeight(8)
   fill(242, 233, 233)
   ellipse(200, 200, 150, 150)

def drawBolt():
   strokeWeight(3)
   fill(255, 234, 0)
   triangle(160, 205, 200, 195, 270, 80)
   triangle(230, 205, 192, 215, 125, 330)
   quad(180, 235, 150, 245, 220, 165, 250, 155)
   strokeWeight(5)
   stroke(255, 234, 0)
   line(194, 195, 215, 170)
   line(198, 215, 183, 232)

def drawHead():
   fill(222, 36, 36)
   noStroke()
   rect(150, 130, 100, 90)
   fill(210, 180, 140)
   ellipse(200, 70, 200, 200)
   fill(222, 36, 36)
   arc(200, 80, 210, 220, 180, 360)

def drawFace():
   stroke(0, 0, 0)
   line(180, 130, 220, 130)
   fill(0, 0, 0)
   ellipse(160, 45, 20, 20)
   ellipse(240, 45, 20, 20)

def draw():
   translate(0, 160)
   drawBackground()
   drawBolt()
   resetMatrix()
   drawHead()
   drawFace()
