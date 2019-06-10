def setup():
    size(400, 400)
    
    global fade
    fade = get()
    noStroke()
    background(0)
    
fade = 0

def draw_circle():
    circle_size = random(5, 10)
    fill(random(220, 255), random(220, 255), 205)
    ellipse(random(0, 400), random(0, 400), circle_size, circle_size)
    
def fading():
    global fade 
    fade = get()
    background(0)
    tint(255, 245)
    image(fade, 0, 0)
    
def draw():
    fading()
    draw_circle()