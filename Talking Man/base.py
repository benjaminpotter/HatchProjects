x = 130
y = 85
paraSize = 50
theKey = ""
space = " "
index = 0
para = ""
frameRate(7)
textAlign(CENTER)
def keyPressed() :
  theKey = key.toString()
  para = para + theKey
  if keyCode == 10 :
    para = ""

def drawCharacter():
  fill(255, 255, 0)
  ellipse(200,220,150,150)
  arc(200, 220, 30, 30, 1, 180)
  fill(0)
  ellipse(160,180,15,15)
  ellipse(240,180,15,15)
  fill(255)
  ellipse(200,70,250,100)

def displayText():
  if para.length > 8 :
    para = ""
  textSize(paraSize)
  fill(0)
  text(para,200,90)

def draw() :
  background(0)
  drawCharacter()
  displayText()
