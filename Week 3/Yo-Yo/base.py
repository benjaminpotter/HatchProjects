def setup():
    size(400, 400)

y = 11
speed = 27

def draw_yoyo():
    global y, speed

    background(252, 255, 214)

    line(200, 0, 200, y)
    fill(255, 0, 115)
    ellipse(200, y, 100, 100)

def move_yoyo():
    global y, speed

    speed -= 1
    y += speed

    if y < 11:
        speed += 2

def draw():
    draw_yoyo()
    move_yoyo()