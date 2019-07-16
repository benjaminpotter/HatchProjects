trackSize = 100;
gameSpeed = 0.2;
carX = 365;
carY = 200;
speedX = 0;
speedY = 0;
carAngle = 0;
turnMod = 40;

isUpPressed = False;
isDownPressed = False;
isRightPressed = False;
isLeftPressed = False;

rectMode(CENTER);
def drawBackground():
    background(0, 255, 0);
    stroke(0);
    strokeWeight(trackSize);
    noFill();
    ellipse(200, 200, 400 - trackSize, 400 - trackSize);

def drawCar():
  fill(255);
  noStroke();
  translate(carX, carY);
  rotate(carAngle);
  rect(0, 0, 10, 20);
  fill(0, 0, 0);
  ellipse(0, -5, 5, 5);
  resetMatrix();

def keyPressed():
  if keyCode == UP:
    isUpPressed = True;
    
  if keyCode == DOWN:
    isDownPressed = True;
  
  if keyCode == LEFT:
    isLeftPressed = True;
  
  if keyCode == RIGHT:
    isRightPressed = True;

def keyReleased() {
  if keyCode == UP:
    isUpPressed = False;
    
  if keyCode == DOWN:
    isDownPressed = False;
  
  if keyCode == LEFT:
    isLeftPressed = False;
  
  if keyCode == RIGHT:
    isRightPressed = False;
    
def steerCar():
    if isLeftPressed == True:
        speedX -= gameSpeed;
    if carAngle <= 90 and carAngle > -90:
        carAngle -= gameSpeed * turnMod;
    if carAngle <= -90 and carAngle > -270:
        carAngle += gameSpeed * turnMod;
    if isRightPressed == true:
        speedX += gameSpeed;
    if carAngle <= 90 and carAngle > -90:
        carAngle += gameSpeed * turnMod;
    if carAngle <= -90 and carAngle > -270:
        carAngle -= gameSpeed * turnMod;
    if isUpPressed == true:
        speedY -= gameSpeed;
    if carAngle <= 180 and carAngle > 0:
        carAngle -= gameSpeed * turnMod;
    if carAngle >= -180 and carAngle < 0:
        carAngle += gameSpeed * turnMod;
    if isDownPressed == true:
        speedY += gameSpeed;
    if carAngle <= 180 and carAngle > 0:
        carAngle += gameSpeed * turnMod;
    if carAngle >= -180 and carAngle < 0:
        carAngle -= gameSpeed * turnMod;
 
    if carAngle > 180:
        carAngle = -180;
    if carAngle <= -270:
        carAngle= 90;

def updateCar():
    carX += speedX;
    carY += speedY;
 
    if speedX > 0:
        speedX -= gameSpeed / 2;
    if speedX < 0:
        speedX += gameSpeed / 2;
    if speedY > 0:
        speedY -= gameSpeed / 2;
    if speedY < 0:
        speedY += gameSpeed / 2;
        
def gameOver():
    if get(carX, carY) != color(0):
        noLoop();
        background(255, 0, 0);
        textSize(40);
        text("GAME OVER", 100, 200);
        
def draw():
    drawBackground();
    steerCar();
    updateCar();
    gameOver();
    drawCar();
