img = getImage("creatures/hopper-happy");
ySpeed = 0;
yPos = 5;
gravity = 1;
hopSpeed = 25;

def drawGround():
    noStroke();
    fill(245, 245, 245);
    rect(0, 325, 400, 75);

def drawFallingCharacter():
    image (img, 200, yPos, 100, 101);
    ySpeed += gravity;
    yPos += ySpeed;

def characterHop():
    if yPos > 222:
        ySpeed = -hopSpeed;

def draw():
    background(255, 255, 255);
    drawGround();
    drawFallingCharacter();
    characterHop();