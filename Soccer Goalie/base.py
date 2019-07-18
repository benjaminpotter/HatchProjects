goalieX = 0
goalieY = 50
goalieSpeed = 15
goalieWidth = 100
goalieHeight = 100
movingLeft = False
movingRight = False
ballRadius = 10
ballSpeed = 15
ballX = random(10, 390)
ballY = 410
numScored = 0
numSaved = 0

def drawScene():
    imageMode(CENTER)
    #image(getImage("avatars/mr-pink"), goalieX, goalieY, goalieWidth, goalieHeight)
    strokeWeight(2)
    fill(255, 255, 255)
    ellipse(ballX, ballY, ballRadius * 2, ballRadius * 2)
    textSize(20)
    textAlign(CENTER, CENTER)
    text(f"Saved\n {numSaved}", 100, 350)
    text(f"Scored\n {numScored}", 300, 350)

def moveGoalie():
    global goalieX
    
    if movingLeft and goalieX > goalieWidth / 2:
        goalieX -= goalieSpeed
    if movingRight and goalieX < 400 - goalieWidth / 2:
        goalieX += goalieSpeed

def moveBall():
    global ballY
    
    ballY -= ballSpeed

def ballCheck():
    global numScored, numSaved
    global ballX, ballY
    
    scored = ballY < -ballRadius
    saved = dist(goalieX, goalieY, ballX, ballY) < ballRadius + goalieHeight / 2

    if scored or saved:
        ballX = random(10, 400 - ballRadius)
        ballY = 400 + ballRadius
    if scored:
        numScored += 1
    if saved:
        numSaved += 1

def keyPressed(e):
    global movingRight, movingLeft
    if keyCode == LEFT:
        movingLeft = True
    elif keyCode == RIGHT:
        movingRight = True

def keyReleased(e):
    global movingRight, movingLeft
    if keyCode == LEFT_ARROW:
        movingLeft = False
    elif keyCode == RIGHT_ARROW:
        movingRight = False

def draw():
    background(78, 153, 78)
    drawScene()
    moveGoalie()
    moveBall()
    ballCheck()
