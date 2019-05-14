def setup():
    size(400, 400)
    
circle_pos = 200
circle_size = 1

def draw():
    global circle_size, circle_pos
    
    background(255)
    
    ellipse(circle_pos, 200, circle_size, circle_size)
    
def mouseClicked():
    global circle_size, circle_pos
    
    circle_pos += 1
    circle_size += 1