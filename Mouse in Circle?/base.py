def setup():
    size(400, 400)
    
circle_color = color(255, 0, 0)
circle_size = 150

def mouseMoved():
    global circle_color, circle_size
    
    if dist(200, 200, mouseX, mouseY) < circle_size / 2:
        circle_color = color(0, 255, 0)
    else:
        circle_color = color(255, 0, 0)
        
def draw_circle():
    global circle_color, circle_size
    
    fill(circle_color)
    ellipse(200, 200, circle_size, circle_size)
    
def draw():
    background(255)
    draw_circle()