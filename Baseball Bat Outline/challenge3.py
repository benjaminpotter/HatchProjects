background(191, 223, 245)
noFill()
strokeWeight(3)

def rotateCanvas():
   resetMatrix()
   translate(200, 200)
   rotate(45)
   translate(-200, -200)
rotateCanvas()

def drawBat():
   bezier(190, 420, 200, 250, 160, 200, 160, 0)
   bezier(210, 420, 200, 250, 240, 200, 240, 0)
   arc(200, 420, 50, 20, 0, 360)
   ellipse(200, 0, 80, 25)
drawBat()

def drawLogo():
   resetMatrix()
   strokeWeight(13)
   arc(-60, 120, 275, 350, 340, 380)
   arc(290, 120, 275, 350, 160, 200)
   line(70, 60, 160, 180)
   line(88, 45, 117, 81)
   line(117, 81, 144, 43)
   line(117, 81, 117, 183)
drawLogo()
