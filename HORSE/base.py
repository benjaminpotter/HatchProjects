score = 0
letterIndex = 0
netRadius = 30
netX = 200
netY = 50
aimL = 50
angle = 0
arrowSpeed = 0.1
textAlign(CENTER, CENTER)
ball = {
    "radius" : 10,
    "x" : 200,
    "y" : 200,
    "speedX" : 0,
    "speedY" : 0,
    "shot" : False
}
def shootBall(angle) :
    global ball
    if ball[shot] == False :
        ball[shot] = True
        ball[speedX] = 12*cos(-angle)
        ball[speedY] = 12*sin(-angle)

def resetBall() :
  global ball
  ball[shot] = False
  ball[speedX] = 0
  ball[speedY] = 0
  ball[x] = random(100,300)
  ball[y] = random(100,300)  

def moveBall() :
  global ball
  ball[x] += ball[speedX]
  ball[y] += ball[speedY]
 
  if dist(ball[x], ball[y], netX, netY) < netRadius :
    score+= 1
    resetBall()
  if ball[y] < 0 or  ball[y] > 400 or ball[x] < 0 or  ball[x] > 400 :
    letterIndex+= 1
    resetBall()



def drawBackground() :
  background(237, 155, 73)
  stroke(255, 255, 255)
  strokeWeight(2)
  noFill()
  arc(200, 150, 100, 100, 360, 540)
  line(150, 150, 250, 150)
  line(150, 150, 150, 0)
  line(250, 150, 250, 0)
  arc(200, 75, 300, 300, 360, 540)
  line(50, 75, 50, 0)
  line(350, 75, 350, 0)

  stroke(0, 0, 0)
  strokeWeight(5)
  fill(247, 134, 145)
  rectMode(CENTER)
  rect(200, netY - netRadius-5, netRadius*3, 10)
  noFill()
  ellipse(netX, netY, netRadius*2, netRadius*2)

def drawBall() :
  global ball
  stroke(0, 0, 0)
  strokeWeight(3)
  fill(255, 157, 0)
  ellipse(ball[x], ball[y], ball[radius]*2, ball[radius]*2)

def drawAim() :
  global ball
  if ball[shot] == False :
    stroke(0, 9, 255)
    strokeWeight(2)
    lineX = ball[x] + aimL*cos(angle)
    lineY = ball[y] - aimL*sin(angle)
    line(ball[x], ball[y], lineX, lineY)
    angle += arrowSpeed
    angle %= 360  

def drawLetters() :
  global ball
  textSize(20)
  fill(0, 0, 0)
  text(f"Score {score}", 300, 40)
  textSize(50)
  text(f"HORSE{[substring(0, letterIndex)]}", 200, 350)
 
  if letterIndex == len("HORSE") :
    text("Restart to Retry", 200, 200)
    noLoop()

def draw() :
  drawBackground()
  drawBall()
  drawAim()
  drawLetters()
  moveBall()

def keyPressed() :
  if key == ' ' :
    shootBall(angle)
