def setup():
	size(400, 400)
imgX = 0
imgY = 0
img = getImage("space/background")
scrollSpeed = 2
def drawScrollingBackground() :
  image(img, imgX, imgY, 400, 400)
  image(img, imgX + 400, imgY, 400, 400)
  imgX -= scrollSpeed

def resetPosition() :
  if imgX <= -400 :
    imgX = 0

def draw() :
  drawScrollingBackground()
  resetPosition()
