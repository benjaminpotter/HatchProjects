noStroke();
rectMode(CENTER);
arrayY = [];
arrayColour = [];
speed = 3;

def setup():
    for i in range(20):
        arrayY.append(400 - i * 20);
        arrayColour.append(color(random(100, 255), random(100, 255), random(100, 255)));
        
def movePiece():
    for i in range(len(arrayY)):
        arrayY[i] += speed;
        if arrayY[i] > 400:
            arrayY[i] = 0;
            arrayColour[i] = color(random(255), random(255), random(255));
        fill(arrayColour[i]);
        rect(200, arrayY[i], arrayY[i], 10, 50);

def draw():
    fill(0, 10);
    rect(200, 200, 400, 400);
    movePiece();
