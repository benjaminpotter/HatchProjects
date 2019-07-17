signLight = FALSE
signColour = color(0, 0, 0)
def drawScene():
  background(0, 153, 255)
  fill(153, 111, 6)
  ellipse(310,240,350,200)
  fill(13, 107, 4)
  rect(0,240,400,160)
  fill(signColour)
  textSize(20)
  text("HOLLYWOOD", 200,190)
def flashSign():
  if signLight==TRUE :
    signColour = color(random(100,200), random(100,200), random(100,200))

def signClick():
  if mouseX>200 and mouseX<330 and mouseY>170 and mouseY<200 :
    signLight=TRUE

def draw():
  drawScene()
  flashSign()

def mouseClicked():
  signClick()
