class Ball:

    def __init__(self):
        self.radius = 20
        self.x = 65
        self.y = 340
        self.speedX = 30
        self.passing = False

    def move(self):
        if self.passing:
            self.x += self.speedX
            if abs(self.x - 200) > 120:
                self.speedX *= -1
                self.passing = False

myBall = Ball()

def drawScene():
    background(155, 207, 207)
    fill(100, 255, 50)
    rect(0, 350, 400, 100)
    fill(0, 0, 0)
    textAlign(CENTER, CENTER)
    textSize(50)
    text("Chest Pass", 200, 100)
    image(getImage("avatars/old-spice-man-blue"), 0, 250)
    image(getImage("avatars/old-spice-man-blue"), 275, 250)
    strokeWeight(3)
    fill(255, 162, 0)
    ellipse(myBall.x, myBall.y, myBall.radius * 2, myBall.radius * 2)

def draw():
    drawScene()
    myBall.move()

def keyPressed():
    if keyCode == 32:
        myBall.passing = true