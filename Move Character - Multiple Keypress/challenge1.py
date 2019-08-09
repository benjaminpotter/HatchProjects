ySpeed = 5
yPos = 150
isUpPressed = False
isDownPressed = False
img = getImage("cute/CharacterPinkGirl")

def keyPressed ():
   global img, isUpPressed, isDownPressed, yPos, ySpeed
   if keyCode == UP :
       isUpPressed = True
  
   if keyCode == DOWN :
       isDownPressed = True

def keyReleased ():
   global img, isUpPressed, isDownPressed, yPos, ySpeed
   if keyCode == UP :
       isUpPressed = False
  
   if keyCode == DOWN :
       isDownPressed = False

def drawCharacter ():
   global img, isUpPressed, isDownPressed, yPos, ySpeed
   image(img, yPos, yPos)

def moveCharacter ():
   global img, isUpPressed, isDownPressed, yPos, ySpeed
   if isUpPressed :
       yPos -= ySpeed
  
   if isDownPressed :
       yPos += ySpeed

def draw ():
   background(255, 255, 255)
   drawCharacter()
   moveCharacter()
