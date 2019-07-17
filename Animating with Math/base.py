iSin = 0;
xSin = 0;
ySin = 0;
iCos = 0;
xCos = 0;
yCos = 0;
iTan = 0;
xTan = 0;
yTan = 0;
fill(0,0,0);

def drawSin():
    position = 100;
    multiplier = 20;
    speed = 5;
    waveSize = 0.15;
    text("SIN: " + round(ySin),180,50);
    ySin = position + sin(iSin)*multiplier;
    xSin += speed;
    iSin += waveSize;
    ellipse(xSin,ySin,10,10);
    if xSin > 400:
        xSin = 0;

def drawCos():
    position = 200;
    multiplier = 20;
    speed = 5;
    waveSize = 0.15;
    text("COS: " + round(yCos),180,150);
    yCos = position + cos(iCos)*multiplier;
    xCos += speed;
    iCos += waveSize;
    ellipse(xCos,yCos,10,10);
    if xCos > 400:
        xCos = 0;

def drawTan():
    position = 350;
    multiplier = 5;
    speed = 5;
    waveSize = 0.04;
    text("TAN: " + round(yTan),180,250);
    yTan = position + tan(iTan)*multiplier;
    xTan += speed;
    iTan += waveSize;
    ellipse(xTan,yTan,10,10);
    if xTan > 400:
        xTan = 0;

def draw():
    background(255);
    drawSin();
    drawCos();
    drawTan();