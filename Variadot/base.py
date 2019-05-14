def setup():
    size(400, 400)
    
circle_size = 1

def draw():
    global circle_size
    
    background(255)
    
    ellipse(200, 200, circle_size, circle_size)
    
def mouseClicked():
    global circle_size
    
    circle_size += 1