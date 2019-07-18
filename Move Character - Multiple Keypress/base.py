ySpeed = 5
yPos = 150
isUpPressed = False
isDownPressed = False
img = getImage("cute/CharacterPinkGirl")
def keyPressed():
  if keyCode == UP:
    isUpPressed = True
  
  if keyCode == DOWN:
    isDownPressed = True
  

def keyReleased():
  if keyCode == UP:
    isUpPressed = False
  
  if keyCode == DOWN:
    isDownPressed = False
  

def drawCharacter():
  image(img, 150, yPos) 

def moveCharacter():
  if (isUpPressed):
    yPos -= ySpeed
  
  if (isDownPressed): 
    yPos += ySpeed
  

def draw():
  background(255, 255, 255)
  drawCharacter()
  moveCharacter()
