start = millis()
score = 0
counter = 0

def displayGame():
    background(0, 252, 0)
    textSize(16)
    text("Click and hold when the number is a multiple of 3", 50, 50)
    textSize(20)
    text("Score: " + score, 165, 350)
    textSize(90)
    text(counter, 185, 200)

def countUp():
    counter = round((millis() - start) / 1000)

def addScore():
    if mouseIsPressed:
        if counter % 3 == 0:
            score += 1
        else:
            score -= 1

def winScreen():
    background(86, 74, 255)
    textSize(37)
    text("You won in " + counter + " seconds!", 10, 200)

def draw():
    if score < 100:
        displayGame()
        countUp()
        addScore()
    else:
        winScreen()