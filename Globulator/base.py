def setup():
      size(400, 400)
def drawGlob():
    if mousePressed:
        x = random(0,50);
        fill(random(0,200), random(0,200), 47)
        ellipse(mouseX, mouseY, x, x)   
