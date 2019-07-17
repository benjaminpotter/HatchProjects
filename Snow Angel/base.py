limbX = 50
swing = 0
speed = 1
maxSwing = 40
fill(0)
background(255)
def drawStickFigure():
    ellipse(200,100,80,80)
    line(200,100,200,250)
    line(200,250,220-limbX-swing,380-swing)
    line(200,250,180+limbX+swing,380-swing)
    line(200,150,180-limbX-swing,200-swing)
    line(200,150,220+limbX+swing,200-swing)

def swingLimbs():
    swing+=speed
    if swing>=maxSwing or swing <= 0 :
        speed = -speed

def draw():
    if mousePressed :
        background(255)
    strokeWeight(20)
    stroke(230)
    drawStickFigure()
    strokeWeight(10)
    stroke(0)
    drawStickFigure()
    swingLimbs()
