ySpeed = 5
yPos = random(0, 400)
img = getImage("avatars/old-spice-man-blue")

def drawCharacter():
   image(img, 200, yPos)

def moveCharacter():
   if keyPressed and keyCode == UP_ARROW :
       yPos = yPos - ySpeed
   if keyPressed and keyCode == DOWN_ARROW :
       yPos = yPos + ySpeed

def draw():
   background(255, 255, 255)
   drawCharacter()
   moveCharacter()
