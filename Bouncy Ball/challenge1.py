def setup():
    size(400, 400)
    
x = random(0, 400)
y = random(0, 400)

x_speed = 5;
y_speed = 1;

def moving_ball():
    global x, y
    global x_speed, y_speed
    
    fill(66)
    ellipse(x, y, 20, 20)
    
    x += x_speed
    y += y_speed
    
def ball_bounce():
    global x, y
    global x_speed, y_speed

    if x < 0 or x > 400:
        x_speed *= -1
    
    if y < 0 or y > 400:
        y_speed *= -1
        
def draw():
    background(127, 204, 255)
    moving_ball()
    ball_bounce()