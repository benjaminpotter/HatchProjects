seconds = 24.0
def drawingSetup() :
  background(0, 0, 0)
  fill(230, 58, 58)
  textFont("Arial", 200)
  textAlign(CENTER, CENTER)

def timerCountdown() :
  seconds -= 1 / 60

def displayTimer() :
  if seconds >= 0 :
    text(seconds.toFixed(1), 200, 200)
  else :
    text("0.0", 200, 200)

def draw() :
  drawingSetup()
  timerCountdown()
  displayTimer()
