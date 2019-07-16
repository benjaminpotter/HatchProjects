clicked = False
magnitude = 0

def drawExplodingCreeper():
    if clicked:
        ellipse(200, 200, magnitude, 170)
        textSize(magnitude / 3)
        text("Sssssssssss...", 34, 365)
        fill(31, 31, 31)
        rect(170, 80, 20, 20)
        rect(210, 80, 20, 20)
        rect(190, 100, 20, 30)
        rect(180, 110, 10, 30)
        rect(210, 110, 10, 30)
        magnitude += 1

def drawRegularCreeper():
    if magnitude < 150:
        noStroke()
        fill(74, 158, 5)
        rect(150, 50, 100, 100)
        rect(163, 148, 76, 139)
        rect(126, 277, 59, 39)
        rect(218, 277, 59, 39)

def explosion():
    if magnitude > 150:
        background(255, 119, 0)
        fill(255, 255, 255)
        textSize(55)
        text("BANG!", 121, 200)

def draw():
    background(255, 255, 255)
    drawRegularCreeper()
    drawExplodingCreeper()
    explosion()

def mouseClicked():
    clicked = True
