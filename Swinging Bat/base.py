batPos = 20
delta = 1
def drawBat() :
  noFill()
  strokeWeight(2)
  var handleWidth = map(180-abs(batPos-200), 0, 180, 0, 30)
  ellipse(200, 200, handleWidth, 30)
  var topWidth = map(180-abs(batPos-200), 0, 180, 0, 50)
  ellipse(batPos, 200, topWidth, 50)
  line(batPos, 175, 200, 195)
  line(batPos, 225, 200, 205)

def rotateBat = function(){
  if batPos > 380 :
    delta = -1
  elif batPos < 20 :
    delta = 1
  batPos += delta

def draw() :
  background(132, 184, 224)
  drawBat()
  rotateBat()
