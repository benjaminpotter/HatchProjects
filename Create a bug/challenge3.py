yPos = 200
ySpeed = 2

def drawBody ():
   global yPos, ySpeed
   background(255, 255, 255)
   fill(90, 175, 80)
   strokeWeight(5)
   ellipse(200, 225, 100, 200)
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

def drawHead ():
   global yPos, ySpeed
   fill(0, 0, 0)
   ellipse(200, 100, 80, 80)
   fill(255, 255, 255)
   ellipse(185, 95, 20, 20)
   ellipse(215, 95, 20, 20)

def draw ():
   global yPos, ySpeed
   drawBody()
   drawHead()
   yPos = yPos + ySpeed
   if yPos == 228 :
       yPos = 200
