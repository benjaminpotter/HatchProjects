def setup():
    size(400, 400)
    
def draw_circle():
    fill(random(255), random(255), random(255))
    ellipse(random(0, 400), random(0, 400), 30, 30)
    
def draw():
    draw_circle()