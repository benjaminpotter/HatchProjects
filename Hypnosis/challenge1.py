def setup():
    size(400, 400)
    set_scene()
    
angle = 0;
radius = 0;
center_x = 200;
center_y = 200;
    
def set_scene():
    background(145, 112, 255)
    stroke(1, 64, 3)
    
def draw_spiraling_circle():
    global angle, radius, center_x, center_y
    
    x = cos(angle) * radius
    y = sin(angle) * radius
    angle = angle + 5
    radius = radius + 0.2
    fill(random(255), random(255), random(255))
    ellipse(x + center_x, y + center_y, 40, 40)
    
def reset_circle():
    global radius
    if radius > 260:
        radius = 0
        
def draw():
    draw_spiraling_circle()
    reset_circle()