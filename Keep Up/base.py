gameOver = False
playerX = 200
playerY = 335
speed = 10
character = getImage("avatars/old-spice-man-blue")
variation = 50
gravity = 1
Ball = {
  "radius" : 10,
  "centerX" : 200,
  "centerY" : 365,
  "speedX" : 0,
  "speedY" : 25
}
def hitRacket () :
  ballAngle = random(90-variation, 90+variation)
  Ball[speedX] = 10*cos(ballAngle)
  Ball[speedY] = 25

def hitWall () :
  Ball[speedX] = -Ball[speedX]

def drawBall () :
  fill(38, 255, 0)
  ellipse(Ball[centerX], Ball[centerY], Ball[radius]*2, Ball[radius]*2)  

def moveBall () :
  Ball[centerX] += Ball[speedX]
  Ball[centerY] -= Ball[speedY]
  Ball[speedY] -= gravity

  if dist(playerX,playerY,Ball[centerX],Ball[centerY]) < 20 :
    hitRacket()

  if Ball[centerX] - Ball[radius] < 0 or Ball[centerX] + Ball[radius] > 400 :
    hitWall()
    
  if 400 - Ball[radius] < Ball[centerY] - Ball[radius] :
    gameOver = True

def drawCharacter () :
  imageMode(CENTER)
  image(character, playerX, playerY)
 
  strokeWeight(2)
  fill(255, 0, 100)
  rectMode(CENTER)
  rect(playerX, 370, 70, 10)

def moveCharacter () :
  if keyPressed and keyCode == LEFT :
    playerX -= speed
  if keyPressed and keyCode == RIGHT :
    playerX += speed

  playerX = constrain(playerX, 35, 365)

def gameOverScreen () :
  fill(102, 0, 255)
  textSize(50)
  textAlign(CENTER, CENTER)
  text("GAME OVER", 200, 100)

def draw () :
  background(244, 196, 119)
  drawCharacter()
  moveCharacter()
  drawBall()
  moveBall()
 
  if gameOver == True :
    gameOverScreen()
    noLoop()
