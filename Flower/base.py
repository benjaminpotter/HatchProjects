numOfPetals = 6;

def drawSetup():
    noStroke();
    translate(width/2, height/2);
    scale(1.4, 1.4);
drawSetup();

def drawBackground():
    background(0,0,200); 
    fill(20, 250, 20);
    rect(-200, 50, 400, 140);
drawBackground();

def drawStem():
    noFill();
    stroke(10, 200, 10);
    strokeWeight(10);
    arc(20, 60, 70, 130, 170, 230);
    noStroke();
drawStem();

def drawPetal():
    fill(200, 19, 200);
    ellipse(0, -20, 20, 30);

def drawFlower():
    for i in range(numOfPetals):
        rotate(360/numOfPetals);
        drawPetal();
drawFlower();

def drawCenter():
    fill(255, 255, 46);
    ellipse(0, 0, 15, 15);
drawCenter();