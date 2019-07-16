ballX=80
ballSpeed=5
def drawScene() :
  background(255, 255, 255)
  bounce = random(-1, 1)
  image(getImage("cute/GrassBlock"), 0, 350, 400, 50)
  image(getImage("cute/CharacterBoy"), 20, 270 + bounce, 80, 120)
  image(getImage("cute/CharacterPinkGirl"), 290, 270 + bounce, 80, 120)

def drawMovingBall() :
  fill(255, 221, 0);
  ellipse(ballX, 365, 20, 20);
  ballX += ballSpeed;

def passBall() :
  if ballX > 300 :
      ballSpeed *= -1
  elif ballX < 80 :
      ballSpeed *= -1

def draw() :
  drawScene()
  drawMovingBall()
  passBall()
