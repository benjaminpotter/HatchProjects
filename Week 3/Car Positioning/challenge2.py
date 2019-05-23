def setup():
    size(400, 400)
    
xPosition = 200
yPosition = 200

def draw_background():
    noStroke()
    background(125, 255, 255)
    fill(68, 255, 0)
    rect(0, 200, 400, 200)
    fill(255, 255, 0)
    ellipse(100, 100, 40, 40)
    fill(255)
    ellipse(280, 80, 40, 40)
    ellipse(300, 85, 45, 45)
    ellipse(270, 95, 40, 40)
    ellipse(285, 95, 30, 30)
    
    ellipse(150, 100, 40, 40)
    ellipse(170, 105, 45, 45)
    ellipse(140, 115, 40, 40)
    ellipse(155, 105, 30, 30)

    fill(66)
    rect(0, 200, 400, 30)
    
def draw_car():
    global xPosition, yPosition
    
    fill(255, 0, 0)
    rect(xPosition, yPosition - 10, 40, 10)
    rect(xPosition + 10, yPosition - 20, 20, 10)
    fill(0, 0, 0)
    ellipse(xPosition + 10, yPosition, 10, 10)
    ellipse(xPosition + 30, yPosition, 10, 10);
    
def draw():
    draw_background();
    draw_car();