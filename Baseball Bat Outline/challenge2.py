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
   stroke(0, 0, 0)
   bezier(190, 420, 200, 250, 160, 200, 160, 0)
   bezier(210, 420, 200, 250, 240, 200, 240, 0)
   arc(200, 420, 50, 20, 0, 360)
   ellipse(200, 0, 80, 25)
drawBat()

def drawBall():
   resetMatrix()
   noStroke()
   fill(255, 255, 255)
   ellipse(300, 300, 100, 100)
drawBall()

def drawStitches():
   stroke(255, 0, 0)
   strokeWeight(10)
   noFill()
   arc(140, 300, 275, 350, 347, 373)
   arc(460, 300, 275, 350, 167, 193)
drawStitches()
