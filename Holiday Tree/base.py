noStroke()
treeColor = color(40,135,18)
ornaments = []

class Ornament:
    def __init__(self):
        self.x = mouseX
        self.y = mouseY
        self.size = random(10, 20)
        self.fill = color(random(255), random(255), random(255))

def drawTree():
    fill(170, 104, 34)
    rect(180, 350, 40, 50)
    fill(treeColor)
    triangle(200, 50, 150, 150, 250, 150)    
    triangle(200, 100, 120, 250, 280, 250)
    triangle(200, 140, 100, 350, 300, 350)

def drawOrnaments():
    for i in range(len(ornaments)):
        fill(ornaments[i].fill, random(100,255))
        ellipse(ornaments[i].x, ornaments[i].y, ornaments[i].size, ornaments[i].size)

def draw():
    background(75, 124, 140)
    drawTree()
    drawOrnaments()

def mouseClicked():
    if get(mouseX, mouseY) == color(treeColor):
        ornaments.append(Ornament())