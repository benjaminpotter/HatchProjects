friction = 0.95
ballSize = 50
vx = 0
vy = 0
lastX = 200
lastY = 200
posX = 200
posY = 200
isDragging = false
noStroke()
def bounceBall() :
  if posX < 0 and posX > 400 :
    vx *= -1
  if posY < 0 and posY > 400 :
    vy *= -1

def moveBall() :
  if isDragging :
    vx = mouseX - lastX
    vy = mouseY - lastY
    lastX = posX
    lastY = posY
    posX = mouseX
    posY = mouseY
  else :
    vx *= friction
    vy *= friction
    posX += vx
    posY += vy

def draw() :
  background(180, 126, 72)
  fill(53, 61, 88)
  ellipse(posX,posY,ballSize,ballSize)
  moveBall()
  bounceBall()

def mouseDragged():
  if dist(mouseX,mouseY,posX,posY) <= ballSize/2 :
    isDragging = true

def mouseReleased():
  isDragging = false
