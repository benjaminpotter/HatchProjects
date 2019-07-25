def drawHoops1():
   noStroke()
   strokeWeight(3)
   fill(100, 150, 255)
   rect(0,0, 400, 200)
   fill(0, 200, 0)
   rect(0, 200, 400, 200)
   stroke(0)
   line(65, 75, 65, 230)
   line(105, 95, 105, 230)
   line(25, 95, 25, 230)
   noFill()
   ellipse(65, 58, 35, 35)
   ellipse(105, 75, 35, 35)
   ellipse(25, 75, 35, 35)

drawHoops1()

def drawStick():
   stroke(200, 120, 75)
   strokeWeight(8)
   line(60, 125, 160, 170)
   line(160, 170, 190, 195)
   line(190, 195, 260, 230)
drawStick()

def drawBroom():
   fill(190, 135, 75)
   stroke(190, 135, 75)
   quad(245, 230, 250, 218, 320, 230, 290, 280)
   strokeWeight(3)
   stroke(0)
   line(253, 216, 245, 235)
   line(260, 217, 251, 239)
drawBroom()

def drawHoops2():
   noFill()
   strokeWeight(8)
   line(360, 310, 360, 400)
   line(240, 345, 240, 400)
   ellipse(360, 253, 110, 110)
   ellipse(240, 290, 110, 110)
drawHoops2()
