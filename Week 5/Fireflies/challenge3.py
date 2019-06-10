def setup():
    size(400, 400)
    
    global fade
    fade = get()
    noStroke()
    background(0)
    
fade = 0

class Firefly:
    def __init__(self):
        self.x = random(0, 400)
        self.y = random(0, 400)
        self.dir = (random(-1, 1), random(-1, 1))
        self.speed = random(0.4, 1) 
        self.rad = random(5, 10)
        
        self.fade = random(100, 255)
        
    def draw_circle(self):
        fill(random(220, 255), random(220, 255), 105, self.fade)
        ellipse(self.x, self.y, self.rad, self.rad)
        self.fade -= 1
        
        
    def update_pos(self):
        self.x += self.dir[0] * self.speed
        self.y += self.dir[1] * self.speed
        
fireflies = []
    
def fading():
    global fade 
    fade = get()
    background(0)
    tint(255, 230)
    image(fade, 0, 0)
    
def draw():
    global fireflies
    
    fading()
    
    if round(random(0, 1)) == 1:
        fireflies.append(Firefly())
    
    for f in fireflies:
        f.update_pos()
        f.draw_circle()