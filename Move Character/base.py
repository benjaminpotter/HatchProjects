def setup():
    size(400, 400)

ySpeed = 5
yPos = random(0, 400)
img = getImage("avatars/old-spice-man")
def drawCharacter():
    global img, yPos
    image(img, 200, yPos)

def moveCharacter():
    global yPos, ySpeed
    if keyPressed and keyCode == UP:
        yPos = yPos - ySpeed
    if keyPressed and keyCode == DOWN:
        yPos = yPos + ySpeed
    
def draw():
    background(255, 255, 255)
    drawCharacter()
    moveCharacter()