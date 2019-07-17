xPos = 20;
yPos = 200;
ballSize = 100;
overtime = False;
textAlign(CENTER,CENTER);

def drawBackground():
    background(170, 115, 42);
    stroke(0);
    line(0,370,400,370);
    
    for y in range(0, 121, 20):
        for x in range(0, 400, 20):
            fill(255);
            ellipse(x,y,15,15);

    line(0,130,400,130)
    fill(255)
    rect(140,50,125,100)
    line(205,150,205,170)
    if overtime == True:
        textSize(40);
        fill(255);
        text("OVERTIME!",210,240);

def drawLowry():
    stroke(255,0,0);
    strokeWeight(4);
    fill(255,255,255);
    rect(-50, 250,150,300,40);
    stroke(0);
    fill(0);
    ellipse(30,190,140,140);
    textSize(150);
    text("7",40,340);

def drawHoop():
    noFill();
    strokeWeight(10);
    stroke(255,0,0);
    arc(205,120,75,20,0,180);
    strokeWeight(1);

def throwBall():
    fill(255, 144, 0);
    ellipse(xPos,yPos,ballSize,ballSize);
    xPos += 4;
    yPos = 400 - (((-1/67)*Math.pow((xPos - 111), 2))+415);
    ballSize -= 2;
    if xPos > 200:
        overtime = True;

def draw():
    drawBackground();
    throwBall();
    drawHoop();
    drawLowry();