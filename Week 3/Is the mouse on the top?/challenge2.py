# REFACTORED

def setup():
    size(400, 400)
    background(255)
    textAlign(CENTER, CENTER)
    
def mouse_on_left():
    if mouseX < 200:
        return True
    return False

def draw():
    textSize(20)
    line(200, 0, 200, 400)
    
    if mouse_on_left():
        fill(0, 255, 0)
        text('Hello?!', random(0, 200), random(400))
    else:
        fill(255, 0, 0)
        text('Goodbye!', random(200, 400),random(400))