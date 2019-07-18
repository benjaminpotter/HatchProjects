class SoccerBall :
  def__init__(self, radius, centerX, centerY, kicked)
  self.radius = 30
  self.centerX = 100
  self.centerY = 340
  self.kicked = False
  def__init__(self, prototype)
  self.prototype = ''
myBall = SoccerBall()
kickStrength = 0

SoccerBall.prototype.kick(strength) :
  self.kicked = True
  self.centerX += (kickStrength+20)/10
  self.centerY -= (kickStrength+20)/10

SoccerBall.prototype.reset() :
  if self.centerX - self.radius > 400 :
    self.kicked = False
    self.centerX = 100
    self.centerY = 340

def drawGround() :
  for i in range (0, 400, 100) :
    image(getImage("cute/GrassBlock"), i, 300)

def drawBall() :
  stroke(0, 0, 0)
  strokeWeight(2)
  fill(255, 255, 255)
  ellipse(myBall.centerX, myBall.centerY,myBall.radius, myBall.radius)

def drawCharacter() :
  image(getImage("avatars/orange-juice-squid"), 0, 230)
  noStroke()
  fill(255, 140, 0)
  rect(10, 210-kickStrength, 50, kickStrength)
  stroke(0, 0, 0)
  strokeWeight(2)
  noFill()
  rect(10, 10, 50, 200)

def checkKick() :
  if !myBall.kicked :
    kickStrength += 3
    kickStrength %= 200  
  else :
    myBall.kick(kickStrength)

def draw() :
  background(163, 205, 214)
  drawGround()
  drawBall()
  drawCharacter()
  checkKick()
  myBall.reset()

#Perform any action that needs to happen on every tick
def keyPressed() :
  if keyCode == 32 :
    myBall.kicked = True
