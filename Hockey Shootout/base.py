goalieImage = getImage("avatars/old-spice-man-blue")
puckX = 200
puckY = 370
puckScale = 1
xSpeed = 0
ySpeed = 0
targetX = -1
targetY = -1
framesToTarget = 20
shootFrame = -1
scaleRate = 0.03
goals = 0
shots = 0
shot = FALSE
shotDone = FALSE
imageMode(CENTER,CENTER)
goalie = {
  “x” : 200,
  “y” : 250,
  “height” : 125,
  “width” : 125,
  “speed” : random(3,5)
}
net = {
  “left” : 90, 
  “right” : 310,
  “top” : 185,
  “bottom” : 300

def scoredGoal():
  puckWidth = 40*puckScale/2
  puckHeight = 15*puckScale/2
  if puckX > net.left and puckX < net.right and puckY > net.top and puckY < net.bottom :
    if puckX > goalie.x-(goalie.width/2) :
      and puckX < goalie.x+(goalie.width/2)
      and puckY > goalie.y-(goalie.height/2)
      and puckY < goalie.y+(goalie.height/2))
      return FALSE
    return TRUE
  else
    return FALSE

def drawBackground():
  stroke(255, 0, 0)
  strokeWeight(3)
  fill(143, 248, 255)
  arc(200,305,300,100,0,180)
  line(0,305,400,305)
  noFill()
  stroke(255, 0, 0)
  strokeWeight(6)
  line(net.left,net.top,net.right,net.top)
  line(net.left,net.top,net.left,net.bottom)
  line(net.right,net.top,net.right,net.bottom)
  noStroke()
  textSize(15)
  fill(0, 0, 0)
  text("Goals: "+goals,5,350)
  text("Shots: "+shots,5,370)
  var percentage = 0
  if shots == 0 :
    percentage = 0
  else :
    percentage = round(goals/shots*100)
  text("Score Percentage: "+percentage+"%",5,390)

def drawGoalie():
  image(goalieImage,goalie.x,goalie.y,goalie.width,goalie.height)
  goalie.x += goalie.speed
  if goalie.x < net.left or goalie.x > net.right :
    goalie.speed = - goalie.speed

def drawPuck():
  noStroke()
  fill(0, 0, 0)
  ellipse(puckX,puckY,40*puckScale,15*puckScale)

def shootPuck():
  if shot :
    puckX += xSpeed
    puckY += ySpeed
    puckScale -= scaleRate
    if frameCount - shootFrame > framesToTarget :
      shot = false
      textSize(50)
      if scoredGoal() :
        text("GOAL!",120,70)
        goals++
      else :
        text("No goal",110,65)
      textSize(15)
      text("Click to reset",155,90)
      shots++
      shotDone = true
      noLoop()

  else :
    textSize(50)
    text("Click to shoot",50,70)

def draw() :
  background(255, 255, 255)
  drawBackground()
  drawGoalie()
  drawPuck()
  shootPuck()

def mouseClicked():
  if !shotDone and !shot :
    targetX = mouseX
    targetY = mouseY
    shot = true
    xSpeed = (targetX-puckX)/framesToTarget
    ySpeed = (targetY-puckY)/framesToTarget
    shootFrame = frameCount
  elif shotDone :
    puckScale = 1
    puckX = 200
    puckY = 370
    shotDone = false
    loop()
