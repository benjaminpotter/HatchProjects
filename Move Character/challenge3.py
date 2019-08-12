ySpeed = 5
yPos = random(0, 400)
img = getImage("avatars/old-spice-man")

def drawCharacter():
   global ySpeed, yPos, img
   image(img, 200, yPos)

def moveCharacter():
   global ySpeed, yPos, img
   if keyPressed and keyCode == UP_ARROW :
       yPos = yPos - ySpeed
   if keyPressed and keyCode == DOWN_ARROW :
       yPos = yPos + ySpeed
   if yPos > 370 or yPos < 0 :
       ySpeed = -ySpeed

def draw():
   background(255, 255, 255)
   drawCharacter()
   moveCharacter()
