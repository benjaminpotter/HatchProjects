def setup():
    size(400, 400)
    textAlign(CENTER, CENTER)
    
start = millis()
milliseconds = 0
seconds = 0
paused = False
pauseTime = 0
pauseStart = 0

def timer():
    global milliseconds, start, seconds, paused, pauseTime, pauseStart
    
    if paused:
        pauseTime = millis() - pauseStart
    else:
        milliseconds = millis() - pauseTime
        seconds = floor(milliseconds / 1000)
    
def displayTime():
    global milliseconds, start, seconds
    
    fill(255, 255, 255)
    textSize(40)
    text("Milliseconds:\n" + str(milliseconds), 200, 140)
    text("Seconds:\n" + str(seconds), 200, 275)
    
def draw():
    background(67, 67, 112)
    timer()
    displayTime()
    
def keyPressed():
    global paused, pauseTime, pauseStart
    if keyCode == 32:
        paused = not paused
        if paused:
            pauseStart = millis()