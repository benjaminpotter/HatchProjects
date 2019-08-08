yPos = 200
ySpeed = 2

def drawEars():
   global yPos, ySpeed
   background(111, 124, 134)
   strokeWeight(10)
   stroke(0)
   strokeWeight(2)
   noFill()
   bezier(27, yPos + 100, 25, yPos + 65, 35, yPos - 10, 0, yPos - 25)
   bezier(160, yPos + 100, 145, yPos + 190, 30, yPos + 200, 27, yPos + 100)
   bezier(0, yPos - 75, 65, yPos - 155, 145, yPos - 20, 175, yPos - 30)
   bezier(373, yPos + 100, 375, yPos + 65, 365, yPos - 10, 400, yPos - 25)
   bezier(240, yPos + 100, 255, yPos + 190, 370, yPos + 200, 373, yPos + 100)
   bezier(400, yPos - 75, 335, yPos - 155, 255, yPos - 20, 225, yPos - 30)

def drawHead():
   global yPos, ySpeed
   fill(111, 124, 134)
   stroke(0)
   triangle(175, 280, 235, 280, 205, 370)
   rect(165, 145, 80, 150, 40)
   rect(150, 240, 110, 60, 40)
   noStroke()
   rect(167, 205, 77, 50)
   rect(183, 252, 44, 50)
   fill(255)
   ellipse(185, 255, 20, 30)
   ellipse(225, 255, 20, 30)
   fill(41, 102, 216)
   ellipse(180, 250, 10, 15)
   ellipse(220, 250, 10, 15)
drawHead()

def draw():
   global yPos, ySpeed
   drawEars()
   drawHead()
   yPos = yPos + ySpeed
   if yPos == 228 :
       yPos = 200
