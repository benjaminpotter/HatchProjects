def setup():
    size(400, 400)

class ball:

    def __init__(self):
        self.x = 200
        self.y = 200
        self.z = 1
        self.size = 50
        self.xspeed = 2
        self.yspeed = 4
        self.zspeed = 0.5

myBall = ball()

def drawScene():
    background(0)
    stroke(255)
    fill(0)
    rect(40, 40, 320, 320)
    line(0, 0, 40, 40)
    line(360, 360, 400, 400)
    line(360, 40, 400, 0)
    line(0, 400, 40, 360)

def moveBall():
    if myBall.z > 40 or myBall.z < 0:
        myBall.zspeed = -myBall.zspeed

    if myBall.x < 0 + myBall.z or myBall.x > 400 - myBall.z:
        myBall.xspeed = -myBall.xspeed

    if myBall.y < 0 + myBall.z or myBall.y > 400 - myBall.z:
        myBall.yspeed = -myBall.yspeed

def drawBall():
    fill(129)
    ellipse(myBall.x, 400 - myBall.z,
            myBall.size - myBall.z, 10 - (myBall.z / 5))
    fill(255)
    ellipse(myBall.x, myBall.y, myBall.size - myBall.z, myBall.size - myBall.z)

def draw():
    drawScene()
    drawBall()
    moveBall()