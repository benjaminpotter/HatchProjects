millSeconds = 0
seconds = 0
minutes = 0
start = True
textAlign(CENTER,CENTER)

def increaseTimer():
    global millSeconds
    if start == True :
        millSeconds+=1

def transferTime():
    global millSeconds
    global seconds
    if millSeconds >= 100 :
        seconds+=1
        millSeconds = 0

    if seconds >= 60 :
        minutes+=1
        seconds = 0

def draw():
    background(0)
    increaseTimer()
    transferTime()
    textSize(60)
    fill(255)
    text(str(minutes) + ":" + str(seconds) + ":" + str(millSeconds), 200, 200)

def mouseClicked(e):
    global start
    start = not start
