allSparks = []
growth = 0.25

class Spark:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 5
        self.angle = random(50,250)
        self.size = random(5,7)
        noStroke()

def setup():
        size(400,400)
        

def moveSparks():
    for i in range(0, len(allSparks)):
        translate(mouseX-40,mouseY-20)
        rotate(allSparks[i].angle)
        allSparks[i].x += allSparks[i].speed
        allSparks[i].y += allSparks[i].speed
        test = random(0,2)
        if(test < 1):
            fill(255,255,0,250)
        else:
            fill(255,0,0,250)
        
        allSparks[i].size -= growth
        ellipse(allSparks[i].x,allSparks[i].y,allSparks[i].size,allSparks[i].size)
        resetMatrix()
  

def drawWand():
    translate(mouseX+10,mouseY+10)
    rotate(210)
    fill(81, 43, 13)
    rect(0,0,60,5,100)

def draw():
    background(0,0,0)
    allSparks.append(Spark())
    drawWand()
    moveSparks()
