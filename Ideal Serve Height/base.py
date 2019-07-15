def setup():
    size(400, 400)
    
hitServe = False;
ballY = 390;
ballVelocity = 6.5;
ballAcceleration = -1;
time = 1;

def updateBall():
    global time, ballY, ballVelocity, ballAcceleration
    time += 0.5;
    ballY -= ballVelocity*time + 0.5*ballAcceleration*time*time;

def bounceBall():
    global ballY, time
    if ballY > 390:
        time = 1;

def highlightBox():
    global ballY
    noStroke();
    fill(255, 245, 99);
    if ballY < 50:
        rect(0, 0, 400, 50)
    elif 50 < ballY and ballY < 200:
        rect(0, 50, 400, 150);    
    else:
        rect(0, 200, 400, 200);    

def drawScene():
    global ballY
    strokeWeight(2);
    stroke(0, 0, 0);
    line(0, 50, 400, 50);
    line(0, 200, 400, 200);
    fill(0, 0, 0);
    textAlign(CENTER,CENTER);
    textSize(30);
    text("Ace", 50, 25);
    text("It's In", 50, 125);
    text("Fault", 50, 300);
    fill(27, 224, 34);
    ellipse(200, ballY, 20, 20);

def draw():
    global hitServe
    background(80, 201, 222);
    if not hitServe:
        updateBall();    
        bounceBall();
    else:
        highlightBox();
    drawScene()

def keyPressed():
    global hitServe
    if keyCode == 32:
        hitServe = not hitServe