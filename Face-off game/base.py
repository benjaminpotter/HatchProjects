puckHeight = 50
dropPuck = false
dropCounter = 28
def drawPuck() :
  noStroke()
  fill(255, 0, 0)
  ellipse(200,350,50,21)
  fill (0, 0, 0, 80)
  ellipse(200,350,10 + puckHeight/8 ,5 + puckHeight / 20)
  fill(0, 0, 0)
  rect(170,puckHeight,60,20,10)

def puckFall() :
  if dropPuck :
    dropCounter --
    if puckHeight <= 320 :
      puckHeight = puckHeight * 1.07
    elif dropCounter != 28 :
    text ("You were " + dropCounter + " milliseconds off!", 114, 50)

def mouseClicked() :
  dropPuck = !dropPuck

def draw() :
  background (255, 255, 255)
  drawPuck()
  puckFall()
