ballHeight = 390
vUp = 4
aG = -0.5
time = 1

def drawTennisBall ():
   global time, aG, vUp, ballHeight
   fill(27, 224, 34)
   ellipse(200, ballHeight, 20, 20)

def calculateBallPosition ():
   global time, aG, vUp, ballHeight
   ballHeight -= vUp * time + 0.5 * aG * time * time
   time += 0.5

def resetBall ():
   global time, aG, vUp, ballHeight
   if ballHeight > 390 :
       ballHeight = 390
       time = 1
  

def draw ():
   drawTennisBall()
   calculateBallPosition()
   resetBall()
   resetMatrix()
   fill(0, 0, 0, 50)
   rect(0, 0, 400, 400)
