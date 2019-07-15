def setup():
    size(400, 400)

green_x = 200
red_x = 400
red_speed = 1

def draw_game():
    background(84, 75, 148)
    
    fill(0, 255, 0)
    rect(green_x, 0, 20, 400)
    
    fill(255, 0, 0)
    rect(red_x, 0, 10, 400)

def move_bar():
    global red_x, red_speed
    red_x -= red_speed
    
def draw():
    draw_game()
    move_bar()

def keyPressed():
    global green_x, red_x, red_speed
    if  keyCode == 32 and red_x > green_x and red_x < green_x + 20:
        red_speed *= 1.2
        red_x = 400
        green_x = random(0, 150)