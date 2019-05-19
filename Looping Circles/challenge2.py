def setup():
    size(400, 400)
    
def draw_circle():
    circle_size = random(30, 50)
    ellipse(random(0, 400), random(0, 400), circle_size, circle_size)
    
def draw():
    draw_circle()