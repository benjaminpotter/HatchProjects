def setup():
    size(400, 400)
    drawGame()

x1 = random(5, 395)
x2 = random(5, 395)
y1 = random(50, 350)
y2 = y1 + random(-50, 50)
midX = (x1 + x2) / 2
midY = (y1 + y2) / 2
clicked = False
distance = 0

def drawGame():
    global x1, y1, x2, y2
    background(255, 255, 255)
    strokeWeight(5)
    stroke(186, 179, 186)
    line(x1, y1, x2, y2)
    fill(143, 143, 143)
    noStroke()
    ellipse(x1, y1, 10, 10)
    ellipse(x2, y2, 10, 10)

def drawPoints():
    global midX, midY
    fill(91, 219, 0)
    ellipse(midX, midY, 10, 10)
    fill(225, 255, 0)
    ellipse(mouseX, mouseY, 5, 5)

def calculateDistance():
    global distance, midX, midY
    distance = round(sqrt(pow((midX - mouseX), 2) + pow((midY - mouseY), 2)))

def drawResults():
    global distance
    fill(97, 97, 97)
    if distance < 3:
        text("WOW you clicked the midpoint!", 50, 50)
    else:
        text("You are off by " + str(distance) + " pixels", 50, 50)

def mousePressed():
    global clicked
    if clicked == False:
        clicked = True
        drawPoints()
        calculateDistance()
        drawResults()
        
def draw():
    return