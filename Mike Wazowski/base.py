def drawBody():
    background(255);
    noStroke();
    fill(236, 237, 208);
    triangle(130, 130, 150, 115, 120, 100);
    triangle(230, 230, 250, 115, 280, 100);
    fill(174, 223, 64);
    ellipse(200, 200, 200, 200);
drawBody();

def drawFace():
  fill(0,0,0);
  arc(200, 270, 60, 50, 180, 360);
  fill(255, 255, 255);
  ellipse(200, 170, 100, 100);
  fill(19, 127, 81);
  stroke(0, 0, 0);
  strokeWeight(2);
  ellipse(200, 170, 50, 50);
  fill(0, 0, 0);
  ellipse(200, 170, 20, 20);
drawFace();

def drawArmsAndLegs():
  strokeWeight(30);
  stroke(174, 223, 64);
  line(100, 200, 90, 300); 
  line(300, 200, 310, 300);
  line(150, 250, 150, 350);
  line(250, 250, 250, 350);
  line(150, 350, 120, 360);
  line(250, 350, 280, 360);
drawArmsAndLegs();