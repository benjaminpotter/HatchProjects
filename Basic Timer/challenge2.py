def setup():
    size(400, 400)
    textAlign(CENTER, CENTER)
    
start = millis()
milliseconds = 0
seconds = 0

def timer():
    global milliseconds, start, seconds
    
    milliseconds = millis() - start
    seconds = floor(((milliseconds / 1000) / 60) / 60)
    
def displayTime():
    global milliseconds, start, seconds
    
    fill(255, 255, 255)
    textSize(40)
    text("Milliseconds:\n" + str(milliseconds), 200, 140)
    text("Hours:\n" + str(seconds), 200, 275)
    
def draw():
    background(67, 67, 112)
    timer()
    displayTime()
    
def keyPressed():
    global start
    if keyCode == 32:
        start = millis()