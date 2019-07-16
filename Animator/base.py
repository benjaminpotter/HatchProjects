circleSize = 20;
animationFrames = [];
frameDrawingX = [];
frameDrawingY = [];
thisFrame = PImage;
numOfFrames = 0;
playBackFrame = 0;
playback = False;
index = 0;

textAlign(CENTER);
def drawSetup():
    fill(255);
    rect(25, 25, 350, 350); 
drawSetup();

def drawText():
    textSize(20);
    fill(0);
    text("Frame: " + numOfFrames, 200, 20);
    textSize(10);
    text("Press Right Arrow To Move Onto Next Frame - Press Space To See Animation", 200, 390);  
drawText();

def playbackAnimation():
    drawSetup();
    tint(255, 255);
    frameRate(10);
    image(animationFrames[playBackFrame], 25, 25, 350, 350);
    playBackFrame += 1;
    if playBackFrame == numOfFrames:
        playback = False;
        playBackFrame = 0;
    
def recordFrame():
    drawSetup();
    for i in range(len(frameDrawingX)):
        fill(0);
        ellipse(frameDrawingX[i], frameDrawingY[i],circleSize,circleSize);

    frameDrawingX = [];
    frameDrawingY = [];
    thisFrame = get(25, 25, 350, 350);
    animationFrames.append(thisFrame);
    
def drawShadow():
    background(255);
    drawSetup();
    tint(255,100);
    image(animationFrames[numOfFrames], 25, 25, 350, 350);
    numOfFrames += 1
    drawText();

def draw():
    if playback == True:
        playbackAnimation();
    else:
        frameRate(60);
        
def keyPressed():
    if keyCode == RIGHT:
        recordFrame();
        drawShadow();        
    if key == ' ':
        playback = True;
        
def mouseDragged():
    if mouseX > 25 and mouseX < 375 and mouseY > 25 and mouseY < 375:
        frameDrawingX.append(mouseX);
        frameDrawingY.append(mouseY);
        fill(0);
        ellipse(mouseX, mouseY, circleSize, circleSize);  