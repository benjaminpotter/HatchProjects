def setup():
    size(400, 400)

lines = []
index = 0

class myLine:

    def __init__(self, y, length):
        self.x = -length
        self.y = y
        self.length = length
        self.speed = random(1, 10)
        self.weight = random(1, 4)
        self.color = color(random(0, 255), random(0, 255), random(0, 255))

def createLines():
    global lines, index
    lines.append(myLine(random(0, 400), random(10, 400)))
    index += 1
    if index > 600:
        index = 0

def drawLines():
    global lines
    for i in range(len(lines)):
        stroke(lines[i].color)
        strokeWeight(lines[i].weight)
        line(lines[i].x, lines[i].y, lines[i].x + lines[i].length, lines[i].y)
        lines[i].x += lines[i].speed

def draw():
    background(0)
    createLines()
    drawLines()
