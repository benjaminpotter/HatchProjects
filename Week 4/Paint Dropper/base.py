def setup():
    size(400, 400)
    
class Drop:
    def __init__(self):
        self.radius = 5
        self.colour = color(random(255), random(255), random(255))
        
    def draw_self(self):
        fill(self.colour)
        ellipse(200, 200, self.radius, self.radius)
        
drops = []

def draw_drops():
    global drops
    
    for d in drops:
        d.radius += 1
        d.draw_self()
        
def draw():
    background(0)
    noStroke()
    draw_drops()
    
def mousePressed():
    global drops
    drops.append(Drop())