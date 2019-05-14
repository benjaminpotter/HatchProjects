def setup():
    size(400, 400)
    display_instructions()
    
def display_instructions():
    fill(46, 46, 46)
    text("click the screen and press a key to start", 92, 200)
    
def display_keycode():
    background(random(75, 255), random(75, 255), random(75, 255))   

    textSize(93)
    text(key, 171, 160)
    
    textSize(27)
    text("that key's code is " + str(keyCode), 72, 257)

def keyPressed():
    display_keycode()

def draw():
    return