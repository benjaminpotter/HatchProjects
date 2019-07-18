yMin = 50;
counter = 0;
pullOver = False;
pull = {'x': 350, 'y': 50}

def drawPull():
    strokeWeight(3);
    line(pull['x'], 0, pull['x'], pull['y']);
    fill(89, 66, 32);
    ellipse(pull['x'], pull['y'] + 20, 20, 50);

def drawDude():
    fill(255,255,255);
    ellipse(185,200,120, 160);
    ellipse(155,200,40,40);
    ellipse(215,200,40,40);
    fill(0,0,0);
    ellipse(155,200,10,10);
    ellipse(215,200,10,10);
    
def drawWackyDude():
    fill(255,255,255);
    ellipse(random(183,187),random(193,203),120, 160);
    ellipse(155,200,40,40);
    ellipse(215,200,40,40);
    fill(0,0,0);
    ellipse(random(140,165),random(190,210),10,10);
    ellipse(random(210,230),random(190,210),10,10);
    
def checkPull():
    global counter, pull, pullOver, yMin
    if counter % 2 == 1:
        pull['y'] = pull['y'] - 5
        if pull['y'] <= yMin:
            pull['y'] = yMin;
            if pullOver == False:
                counter += 1;
                pullOver = True;
        if pull['y'] > yMin:
            pullOver = False;
            background(random(0,255), random(0,255), random(0,255));
            drawWackyDude();
            drawPull();
    
def draw():
    background(147, 191, 184);
    drawPull();
    drawDude();
    checkPull();

def mouseDragged(e):
    global pull, counter
    if counter % 2 == 0:
        pull['y'] = mouseY;

def mouseReleased(e):
    global counter
    counter += 1