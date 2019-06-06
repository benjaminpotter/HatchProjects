def setup():
    size(400, 400)
    
x_speed = 3
y_speed = 4
x_pos = 0
y_pos = 200

def draw_ball():
    global x_pos, y_pos
    global x_speed, y_speed
    
    stroke(255, 0, 0)
    strokeWeight(15)
    point(x_pos, y_pos)
    x_pos += x_speed
    y_pos += y_speed
    
def loop_ball():
    global x_pos, y_pos
    
    if x_pos > 412:
        x_pos = -12
    elif y_pos > 412:
        y_pos = - 12
        
def draw():
    background(100)
    draw_ball()
    loop_ball()
