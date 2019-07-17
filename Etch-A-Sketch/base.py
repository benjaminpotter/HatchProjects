x = 200;
y = 200;
speed = 5;


def setup():
    size(400, 400)
    textAlign(CENTER, CENTER);
    drawBackground()

def drawBackground():
    background(255, 0, 0);
    fill(184, 167, 167);
    rect(25, 25, 350, 300);
    fill(255, 255, 255);
    ellipse(50, 360, 50, 50);
    ellipse(350, 360, 50, 50);
    fill(221, 255, 0);
    textSize(30);
    text("ETCH A SKETCH", 200, 360);
    
def draw(): 
    fill (0, 0, 0)
    rect(x, y, speed, speed)

def mouseClicked(): 
  fill(184, 167, 167)
  rect(25, 25, 350, 300)

def keyPressed(): 
    if keyCode == RIGHT and x < 350:
        x += speed
    elif keyCode == UP and y > 26: 
        y -= speed
    elif keyCode == LEFT and x > 26: 
        x -= speed
    elif keyCode == DOWN and y < 325: 
        y += speed
  
