def drawBorder():
   fill(30, 10, 240)
   rect(0, 0, 40, 400)
   rect(0, 0, 400, 40)
   rect(360, 0, 40, 400)
   rect(0, 360, 400, 40)
drawBorder()

def drawCircle():
    noStroke()
    fill(0, 0, 0)
    ellipse(200, 200, 300, 300)
    fill(210, 0, 0)
    ellipse(200, 200, 250, 250)
drawCircle()

def drawX():
   fill(0, 0, 0)
   quad(111, 100, 95, 130, 300, 310, 320, 280)
   quad(290, 100, 310, 130, 115, 300, 85, 275)
drawX()
