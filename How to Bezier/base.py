startX = 100
startY =100
endX = 300
endY = 300
controlPoint1x = 150
controlPoint1y = 150
controlPoint2x = 250
controlPoint2y = 250
moveSpeed = 5
text1x = 0
text1y = 0
text2x = 0
text2y = 0
def drawText():
  if(controlPoint1x < 350 and controlPoint1x > 0 and controlPoint1y < 400 and controlPoint1y > 30):
    text1x = controlPoint1x
    text1y = controlPoint1y
  
  if(controlPoint2x < 350 and controlPoint2x > 0 and controlPoint2y < 400 and controlPoint2y > 30):
    text2x = controlPoint2x
    text2y = controlPoint2y
  
  fill(0,0,0)
  strokeWeight(0)
  text(f"({startX}, {startY})", startX+2,startY-8)  
  text(f"({endX}, {+endY})", endX+2,endY+15)
  text(f"({controlPoint1x}),{controlPoint1y})",text1x+2,text1y-8)  
  text(f"({controlPoint2x}),{controlPoint2y})",text2x+2,text2y-8)

def drawShapes():
  noFill()
  strokeWeight(10)
  background(255)
  stroke(0)
  bezier(startX, startY, controlPoint1x, controlPoint1y, controlPoint2x, controlPoint2y, endX, endY)
  stroke(255,0,0)
  strokeWeight(10)
  point(controlPoint1x,controlPoint1y)
  point(controlPoint2x,controlPoint2y)

def draw():
  drawShapes()
  drawText()

def keyPressed():
  if(keyCode == LEFT):
    controlPoint1x -= moveSpeed
  
  if(keyCode == RIGHT):
    controlPoint1x += moveSpeed
  
  if(keyCode == UP):
    controlPoint1y -= moveSpeed
  
  if(keyCode == DOWN):
    controlPoint1y += moveSpeed
  
  if(key == 'a'):
    controlPoint2x -= moveSpeed
  
  if(key == 'd'):
    controlPoint2x += moveSpeed
  
  if(key == 'w'):
    controlPoint2y-= moveSpeed
  
  if(key == 's'):
    controlPoint2y += moveSpeed
  
