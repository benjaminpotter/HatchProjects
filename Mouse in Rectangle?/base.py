def setup():
    size(400, 400)
    
rect_colour = color(255, 0, 0)

def check_mouse_position():
    global rect_colour
    
    if mouseX > 100 and mouseX < 300 and mouseY > 150 and mouseY < 250:
        rect_colour = color(0, 255, 0)
    else:
        rect_colour = color(255, 0, 0)
        
def draw_rect():
    global rect_colour
    fill(rect_colour)
    rect(100, 150, 200, 100)
    
def mouseMoved():
    check_mouse_position()
        
def draw():
    draw_rect()