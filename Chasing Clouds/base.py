locationX = []
locationY = []
positionCounter = 0
playbackCounter = 0
released = FALSE
def playback() :
  background(0,200,255)
  ellipse(locationX[playbackCounter],locationY[playbackCounter],100,50)
  ellipse(locationX[playbackCounter]+20,locationY[playbackCounter]-25,100,50)
  ellipse(locationX[playbackCounter]+40,locationY[playbackCounter],100,50)  
  playbackCounter++
  if playbackCounter == positionCounter :
    playbackCounter = 0
    positionCounter = 0
    released = FALSE

def mouseDragged():
  ellipse(mouseX, mouseY, 20, 20)
  locationX[positionCounter] = mouseX
  locationY[positionCounter] = mouseY
  positionCounter++

def mouseReleased():
  released = TRUE

background(0,200,255)
def draw():
    noStroke()
  if released == TRUE :
    playback()
