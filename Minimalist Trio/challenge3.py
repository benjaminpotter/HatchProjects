def drawMain(x) :
   fill(0, 0, 0)
   ellipse(x, 270, 60, 150)
   fill(247, 225, 192)
   ellipse(x, 200, 75, 75)
   fill(0, 0, 0)

def drawCrabbe() :
   drawMain(100)
   noFill()
   stroke(0, 0, 0)
   strokeWeight(3)
   fill(0, 0, 0)
   noStroke()
   arc(100, 192, 75, 75, 180, 360)
   triangle(63, 192, 80, 192, 68, 205)
drawCrabbe()

def drawGoyle() :
   drawMain(200)
   fill(109, 71, 13)
   ellipse(193, 180, 35, 35)
   ellipse(215, 180, 35, 35)
   ellipse(180, 190, 35, 35)
   ellipse(225, 190, 35, 35)
drawGoyle()

def drawMalfoy() :
   drawMain(300)
   translate(300, 200)
   rotate(30)
   fill(255, 255, 153)
   ellipse(-25, 0, 30, 60)
   rotate(-70)
   ellipse(20, 0, 45, 75)
drawMalfoy()
