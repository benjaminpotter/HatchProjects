def setup():
    size(400, 400)
    background(255)
    
    setup_scene()

last_square = 0
current_square = 0 

square_color = [color(random(255), random(255), random(255)), color(random(255), random(255), random(255)), color(random(255), random(255), random(255)), color(random(255), random(255), random(255))]

locked_squares = []

def setup_scene():
    strokeWeight(5)
    line(200, 0, 200, 400)
    line(0, 200, 400, 200)
    
def set_color():
    fill(square_color[current_square - 1])
     
def change_color():
    global last_square, current_square
    
    if last_square != current_square and not current_square in locked_squares:
        square_color[current_square - 1] = color(random(255), random(255), random(255))
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
        
def mouseClicked(e):
    if current_square in locked_squares:
        locked_squares.remove(current_square)
    else:
        locked_squares.append(current_square)
        
def draw():
    set_color()
    change_color()
    draw_squares()
