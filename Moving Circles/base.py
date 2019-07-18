x = 100
y = 200
xSpeed = 3
ySpeed = 3
onTop = False
def moveCircles():
    global x
    global xSpeed
    global y 
    global ySpeed
    global onTop
    x += xSpeed
    if(x > 300 or x < 100):
        xSpeed *= -1
        onTop = not onTop

 
    y += ySpeed
    if(y > 300 or y < 100):
        ySpeed *= -1

def drawCircles():
    if onTop:
        fill(71)
        ellipse(x, height/2, y/2+10, y/2+10)
        fill(255, 255, 255)
        ellipse(width-x, height/2, ((height-y)/2)+10, ((height-y)/2)+10)
  
    if not onTop:
        fill(255, 255, 255)
        ellipse(width-x, height/2, ((height-y)/2)+10, ((height-y)/2)+10)
        fill(71)
        ellipse(x, height/2, y/2+10, y/2+10)
  
def draw():
    background(88, 180, 188)
    moveCircles()
    drawCircles()
