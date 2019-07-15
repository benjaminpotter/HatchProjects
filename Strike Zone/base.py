def setup():
    size(400, 400)
    draw_scene()

def draw_scene():
    background(45, 120, 39)
    
    noFill()
    strokeWeight(10)
    rect(125, 100, 150, 200)
    
    textSize(20)
    text("Click anywhere to pitch the ball.", 70, 50)
    
def pitchBall():
    if mouseX > 125 and mouseX < 275 and mouseY > 100 and mouseY < 300:
        stroke(255, 0, 0)
    else:
        stroke(255)
    strokeWeight(20)
    point(mouseX, mouseY)
    
def mousePressed():
    pitchBall()
    
def draw():
    return
