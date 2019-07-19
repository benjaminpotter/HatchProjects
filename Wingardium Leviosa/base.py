index = 0
manyTargets = []
def target(x,y):
  this.x = x
  this.y = y
  this.hit = FALSE

manyTargets.push(new target(40,270))
manyTargets.push(new target(200,320))
manyTargets.push(new target(360,270))
manyTargets.push(new target(200,40))
manyTargets.push(new target(200,380))

def isHit():
  for i in range (0, manyTargets.length):
    if dist(mouseX,mouseY,manyTargets[i].x,manyTargets[i].y) < 20 :
      manyTargets[i].hit = TRUE

def checkSpell():
  for i in range (0, manyTargets.lengthi++):
    if manyTargets[i].hit == FALSE :
      return FALSE
  return TRUE

def drawTrail() :
  stroke(255,255,255,10)
  strokeWeight(5)
  noFill()
  arc(200,270,320,100,0,180)
  line(360,270,200,40)
  line(200,40,200,380)

def drawSpell() :
  fill(255)
  textSize(30)
  for i in range (0, 30):
    circleSize = random(2,10)
    ellipse(random(0,400),random(0,400),circleSize,circleSize)
  text("WINGARDIUM LEVIOSA!",30,200)

def draw() :
 background(66,66,66)
 drawTrail()
 if checkSpell() == TRUE :
   drawSpell()

def mouseDragged() :
  ellipse(mouseX,mouseY,20,20)
  isHit()

def mouseReleased() :
  checkSpell()
  for(0, manyTargets.length):
    manyTargets[i].hit = false
