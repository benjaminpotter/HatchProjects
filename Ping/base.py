drops = []
class Drop:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        self.speed = random(2, 6)

background(0, 246, 255)

def draw():
    global drops
    
    noStroke()
    fill(30, 198, 204, 40)
    rect(0, 0, 400, 400)
    noFill()
    strokeWeight(4)
    stroke(220, 220, 255)
    for i in range(len(drops)):
        ellipse(drops[i].x, drops[i].y, drops[i].radius, drops[i].radius)
        drops[i].radius += drops[i].speed

def mouseClicked(e):
    drops.append(Drop(mouseX, mouseY))
