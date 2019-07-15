def setup():
    size(400, 400)
    setupConfetti()

numOfConfetti = 500
yPos = []
xPos = []
gSpeed = []
gColor = []

def setupConfetti():
    global numOfConfetti, yPos, xPos, gSpeed, gColor

    for i in range(numOfConfetti):
        yPos.append(random(-200,0))
        xPos.append(random(0,400))
        gSpeed.append(random(2,10))
        gColor.append(color(random(0,255),random(0,255),random(0,255), random(80,255)))
    
def drawConfetti():
    global yPos, xPos, gColor, gSpeed
    
    for i in range(len(yPos)):
        if yPos[i] < 370:
            gSpeed[i] += 0.1
            yPos[i] += gSpeed[i]
        fill(gColor[i])
        ellipse(xPos[i], yPos[i], 20, 20)
        
def draw():
    background(0,0,0)
    noStroke()
    drawConfetti()