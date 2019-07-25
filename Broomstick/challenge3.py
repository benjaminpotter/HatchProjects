var drawStick() :
   background(100, 150, 255)
   stroke(200, 120, 75)
   strokeWeight(8)
   line(60, 125, 160, 170)
   line(160, 170, 190, 195)
   line(190, 195, 260, 230)

drawStick()

var drawBroom() :
   fill(190, 135, 75)
   stroke(190, 135, 75)
   quad(245, 230, 250, 218, 320, 230, 290, 280)
   strokeWeight(3)
   stroke(0)
   line(253, 216, 245, 235)
   line(260, 217, 251, 239)

drawBroom()

var drawHarry() :
   fill(0, 0, 0)
   rect(162, 168, 30, 150)
   ellipse(170, 325, 50, 20)
   fill(255, 255, 255)
   noStroke()
   rect(157, 72, 40, 130, 10)
   stroke(255, 255, 255)
   strokeWeight(20)
   line(120, 150, 170, 100)
   fill(210, 180, 140)
   noStroke()
   rect(166, 53, 20, 20)
   ellipse(176, 30, 45, 55)
   ellipse(115, 155, 20, 20)
   fill(0, 0, 0)
   triangle(181, 72, 350, 160, 320, 200)
   triangle(190, 80, 290, 200, 320, 180)
   triangle(180, 71, 320, 150, 350, 100)
   arc(180, 38, 60, 70, 270, 450)

drawHarry()
