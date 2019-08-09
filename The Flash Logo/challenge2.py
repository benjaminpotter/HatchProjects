def drawBackground():
   background(222, 36, 36)
   stroke(0, 0, 0)
   strokeWeight(8)
   fill(242, 233, 233)
   ellipse(200, 200, 150, 150)

def drawBolt():
   colour1 = random(0, 255)
   colour2 = random(0, 255)
   colour3 = random(0, 255)
   strokeWeight(3)
   fill(colour1, colour2, colour3)
   triangle(160, 205, 200, 195, 270, 80)
   triangle(230, 205, 192, 215, 125, 330)
   quad(180, 235, 150, 245, 220, 165, 250, 155)
   strokeWeight(5)
   stroke(colour1, colour2, colour3)
   line(194, 195, 215, 170)
   line(198, 215, 183, 232)

def draw():
   drawBackground()
   drawBolt()
