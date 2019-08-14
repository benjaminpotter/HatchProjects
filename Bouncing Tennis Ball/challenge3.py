ballHeight = 390
vUp = 4
aG = -0.5
time = 1
xPos = 200
xSpeed = 2

def drawTennisBall():
   global xPos, xSpeed, time, aG, vUp, ballHeight
   fill(27, 224, 34)
   ellipse(xPos, ballHeight, 20, 20)

def calculateBallPosition():
   global xPos, xSpeed, time, aG, vUp, ballHeight
   ballHeight -= vUp * time + 0.5 * aG * time * time
   time += 0.5 
   if keyIsPressed and keyCode == RIGHT_ARROW :
       xPos = xPos + xSpeed
  
   if keyIsPressed and keyCode == LEFT_ARROW :
       xPos = xPos - xSpeed
  
   if xPos > 400 :
       xPos = 0
  
   if xPos < 0 :
       xPos = 400

def resetBall():
   global xPos, xSpeed, time, aG, vUp, ballHeight
   if ballHeight > 390 :
       ballHeight = 390
       time = 1

def draw():
   background(80, 201, 222)
   drawTennisBall()
   calculateBallPosition()
   resetBall()
