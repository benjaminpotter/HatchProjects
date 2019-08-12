def drawCircle():
    noStroke()
    fill(0, 0, 0)
    ellipse(200, 200, 300, 300)
    fill(210, 0, 0)
    ellipse(200, 200, 250, 250)

def drawX():
   fill(0, 0, 0)
   quad(111, 100, 95, 130, 300, 310, 320, 280)
   quad(290, 100, 310, 130, 115, 300, 85, 275)

def draw():
   background(random(0, 255), random(0, 255), random(0, 255))
   drawCircle()
   drawX()
