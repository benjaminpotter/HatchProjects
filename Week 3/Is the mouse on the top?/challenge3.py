# REFACTORED

def setup():
    size(400, 400)
    background(255)
    textAlign(CENTER, CENTER)
    
def mouse_on_left():
    if mouseX < 200:
        return True
    return False

def mouse_on_top():
    if mouseY < 200:
        return True
    return False

def draw():
    textSize(20)
    line(200, 0, 200, 400)
    line(0, 200, 400, 200)
    
    if mouse_on_left() and mouse_on_top():
        fill(0, 255, 0)
        text('Top Left', random(0, 200), random(0, 200))
    elif mouse_on_left() and mouse_on_top() == False:
        fill(255, 0, 0)
        text('Bottom Left', random(0, 200), random(200, 400))
    elif mouse_on_left() == False and mouse_on_top():
        fill(0, 0, 255)
        text('Top Right', random(200, 400), random(0, 200))
    else:
        fill(255, 255, 0)
        text('Bottom Right', random(200, 400), random(200, 400))