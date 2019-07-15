# REFACTORED

def setup():
    size(400, 400)
    background(255)
    textAlign(CENTER, CENTER)
    
def mouse_on_top():
    if mouseY < 200:
        return True
    return False

def draw():
    textSize(20)
    line(0, 200, 400, 200)
    
    if mouse_on_top():
        fill(0, 255, 0)
        text('YES!', random(400), random(0, 200))
    else:
        fill(255, 0, 0)
        text('NO!', random(400), random(200, 400))