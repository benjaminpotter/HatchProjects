class Baseball:

    def __init__(self):
        self.diameter = 50
        self.x = random(self.diameter / 2, (400 - self.diameter / 2))
        self.y = random(self.diameter / 2, (400 - self.diameter / 2))

    def drawBall(self):
        self.diameter += 10
        noStroke()
        fill(255)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noFill()
        stroke(255, 0, 0)
        strokeWeight(self.diameter / 50)
        arc(self.x - self.diameter / 1.5, self.y,
            self.diameter, self.diameter, -45, 45)
        arc(self.x + self.diameter / 1.5, self.y,
            self.diameter, self. diameter, 135, 225)

hits = 0
strikes = 0
myBaseball = Baseball()

def hitBaseball():
    global myBaseball
    global hits, strikes

    if myBaseball.diameter >= 300:
        d = dist(myBaseball.x, myBaseball.y, mouseX, mouseY)
        if d < 30:
            hits += 1
        else:
            strikes += 1
            myBaseball = Baseball()

def drawScore():
    fill(255, 0, 0)
    textAlign(CENTER, CENTER)
    textSize(30)
    text("Hits:\n" + str(hits), 50, 350)
    text("Strikes\n" + str(strikes), 350, 350)


def strikeOut():
    if strikes == 3:
        background(204, 204, 204)
        fill(255, 0, 0)
        textSize(50)
        text("Three Strikes\nYou're Out!", 200, 200)
        noLoop()


def draw():
    background(156, 202, 214)
    myBaseball.drawBall()
    hitBaseball()
    drawScore()
    strikeOut()
