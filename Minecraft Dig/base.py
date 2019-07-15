def setup():
	size(400, 400)
xPos = 0
yPos = 0
pixelSize = 20
def drawBackground() :
noStroke()
background(128, 187, 231)
fill(118, 74, 47)
rect(0,100, 400, 400)
fill(102, 150, 88)
rect(0, 100, 400, 50)

drawBackground()

def draw() :
  if mouseIsPressed :
    xPos = floor(mouseX / pixelSize) * pixelSize
    yPos = floor(mouseY / pixelSize) * pixelSize
    fill(128, 187, 231)
    rect(xPos, yPos, pixelSize, pixelSize)
