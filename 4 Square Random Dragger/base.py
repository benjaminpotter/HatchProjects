def setup():
    size(400, 400)
    background(255)
    
    setup_scene()

last_square = 0
current_square = 0

def setup_scene():
    strokeWeight(5)
    line(200, 0, 200, 400)
    line(0, 200, 400, 200)
    
def change_colour():
    global last_square, current_square
    if last_square != current_square:
        fill(random(0, 255), random(0, 255), random(0, 255))
        last_square = current_square

def draw_squares():
    global current_square
    
    if mouseX < 200 and mouseY < 200: 
        rect(0, 0, 200, 200)
        current_square = 1
    elif mouseX < 200 and mouseY > 200:
        rect(0, 200, 200, 200)
        current_square = 2
    elif mouseX > 200 and mouseY < 200:
        rect(200, 0, 200, 200)
        current_square = 3
    elif mouseX > 200 and mouseY > 200:
        rect(200, 200, 200, 200)
        current_square = 4
        
def draw():
    change_colour()
    draw_squares()