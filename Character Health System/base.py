invincible = False
gameOver = False
maxLives = 5
numLives = maxLives

def hurtPlayer():
    if not invincible:
        numLives -= 1

def healPlayer():
    if not gameOver and numLives < maxLives:
        numLives -= 1

def checkGameOver():
    if numLives <= 0:
        numLives = 0
        gameOver = True

def drawLives():
    for i in range(maxLives):
        if i < numLives:
            image(getImage("space/healthheart"), 10 + 30 * i, 10, 30, 30)
        else:
            image(getImage("space/minus"), 10 + 30 * i, 10, 30, 30)

    if invincible:
        image(getImage("cute/Star"), 5, 30, 40, 60)

def displayCharacterState():
    fill(0, 0, 0)
    textAlign(CENTER, CENTER)
    textSize(35)
    if not gameOver:
        text("Your character is alive.\nPlay!", 200, 200)
    else:
        text(
            "Your character is dead.\nGame Over!\n(must restart game)", 200, 200)

def draw():
    image(getImage("space/background"), 0, 0, 400, 400)
    drawLives()
    checkGameOver()
    displayCharacterState()

def keyPressed():
    if keyCode == 37:
        hurtPlayer()
    if keyCode == 39:
        healPlayer()
    if keyCode == 32 and not gameOver:
        invincible = not invincible
