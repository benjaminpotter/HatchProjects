def setup():
    size(400, 400)
    textAlign(CENTER,CENTER)

start = millis()
score = 0
counter = 0

def displayGame():
    global score, counter

    background(0, 252, 0)
    textSize(16)
    text("Click and hold when the number is a multiple of 3", 200, 50)
    textSize(20)
    text("Score: " + str(score), 200, 350)
    textSize(90)
    text(counter, 200, 200)


def countUp():
    global counter, start
    counter = int((millis() - start) / 1000)


def addScore():
    global counter, score
    if mousePressed:
        if counter % 7 == 0:
            score += 1
        else:
            score -= 1

def winScreen():
    global counter
    background(86, 74, 255)
    textSize(37)
    text("You won in " + counter + " seconds!", 200, 200)

def draw():
    global score
    if score < 100:
        displayGame()
        countUp()
        addScore()
    else:
        winScreen()
