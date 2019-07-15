def setup():
    size(400, 400)
    set_scene()
    
angle = 0;
radius = 0;
center_x = 200;
center_y = 200;
    
def set_scene():
    background(random(255), random(255), random(255))
    stroke(random(255), random(255), random(255))
    fill(random(255), random(255), random(255))
    
def draw_spiraling_circle():
    global angle, radius, center_x, center_y
    
    x = cos(angle) * radius
    y = sin(angle) * radius
    angle = angle + 5
    radius = radius + 0.2
    ellipse(x + center_x, y + center_y, 40, 40)
    
def reset_circle():
    global radius
    radius = 0
    set_scene()
        
def draw():
    global center_x, center_y, radius
    
    center_x = mouseX
    center_y = mouseY
    
    draw_spiraling_circle()
    
    if radius > 260:
        reset_circle()
        
def mousePressed():
    reset_circle()