xPos = 200
xSpeed = 2

def drawFootball():
   global xPos, xSpeed
   fill(161, 128, 27)
   bezier(xPos - 150, 200, xPos - 100, 75, xPos +100, 75, xPos + 150, 200)
   bezier(xPos - 150, 200, xPos - 100, 325, xPos +100, 325, xPos +150, 200)

def drawStitches():
   global xPos, xSpeed
   noFill()
   stroke(255, 255, 255)
   strokeWeight(10)
   arc(xPos, 170, 150, 20, 180, 360)
   line(xPos, 150, xPos, 170)
   line(xPos - 50, 150, xPos - 45, 170)
   line(xPos + 50, 150, xPos + 45, 170)
   strokeWeight(10)
   arc(xPos - 108, 200, 31, 100, 270, 440)
   arc(xPos + 118, 200, 31, 100, 115, 251)

def draw():
   global xPos, xSpeed
   background(50, 130, 13)
   drawFootball()
   drawStitches()
   xPos = xPos + xSpeed
   if xPos > 450 :
       xPos = 0
