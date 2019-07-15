flip = true
def setColour() :
  if flip :
    fill(255, 255, 255)
  else :
    fill(0, 100, 150)

def mouseClicked() :
  flip =! flip

def draw() :
  background(191, 191, 191)
  setColour()
  rect(100, 100, 200, 200)
