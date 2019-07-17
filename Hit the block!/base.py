numHits = 10
imageBeingHit = getImage("minecraft/block-grass")
imageHitting = getImage("minecraft/pickaxe-diamond")
angle = -45
xPosition = 100
def drawImages() :
  image(imageBeingHit, 300, 200, 200, 200)
  translate(xPosition,150)
  rotate(angle)
  tint(255,255)
  image(imageHitting, 0, 0, 200, 200)
  resetMatrix()

def hitBlock() :
  if mouseIsPressed :
    angle = 0
    xPosition = 200
    tint(100,100,100)
  else :
    angle = -45
    xPosition = 100

def endScreen():
  background(0, 0, 0)
  text("You gained 1 dirt", 200, 200)

#Draw a screen that is displayed when the item is destroyed.

def drawText() :
  textAlign(CENTER,CENTER)
  textSize(20)
  text("Hit the block " + numHits + " more times", 200, 350)

def draw():
  imageMode(CENTER,CENTER)
  background(0, 0, 0)
  hitBlock()
  drawImages()
  drawText()
  if numHits < 1 :
    endScreen()

def mouseClicked():
  numHits -= 1
