ySpeed = 5
xSpeed = 5
yPos = random(0, 400)
xPos = random(0, 400)
img = getImage("avatars/old-spice-man")

def drawCharacter():
   global ySpeed, xSpeed, yPos, xPos, img
   image(img, xPos, yPos)

def moveCharacter():
   global ySpeed, xSpeed, yPos, xPos, img
   if keyPressed and keyCode == UP_ARROW :
       yPos = yPos - ySpeed
   if keyPressed and keyCode == DOWN_ARROW :
       yPos = yPos + ySpeed
   if keyPressed and keyCode == RIGHT_ARROW :
       xPos = xPos + xSpeed;
   if keyPressed and keyCode == LEFT_ARROW :
       xPos = xPos - xSpeed

def draw():
   background(255, 255, 255)
   drawCharacter()
   moveCharacter()
