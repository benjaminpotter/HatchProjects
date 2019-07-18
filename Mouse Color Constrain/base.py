amountOfRed = 0

def displayText():
    fill(0, 0, 0)
    textSize(30)
    text("MouseX: " + mouseX, 100, 200)
    text("Amount of Red: " + round(amountOfRed), 70, 250)

def mapRed():
    amountOfRed = map(mouseX, 0, 400, 0, 255)

def draw():
    background(amountOfRed, 0, 0)
    mapRed()
    displayText()