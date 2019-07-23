# MAP FUNCTION NEEDS EDITING

background(255)

last_square = 0
current_square = 0 

square_color = []
locked_squares = []

horizontal_squares = 16
vertical_squares = 16

def setup_scene():
    for i in range(horizontal_squares * vertical_squares):
        square_color.append(color(random(255), random(255), random(255)))

def set_color():
    fill(square_color[current_square - 1])
     
def change_color():
    global last_square, current_square
    
    if last_square != current_square and not current_square in locked_squares:
        square_color[current_square - 1] = color(random(255), random(255), random(255))
        last_square = current_square
        
def set_current_square():
    x = map(mouseX, 0, 400, 1, 16) # !!!!!
    y = map(mouseY, 0, 400, 1, 16)
    
    return floor(x * y) 
 
def draw_squares():
    global current_square
    
    for x in range(horizontal_squares):
        for y in range(vertical_squares):
            rect(x * (width / horizontal_squares), y * (height / vertical_squares), width / horizontal_squares, height / vertical_squares)
    
        
def mouseClicked(e):
    if current_square in locked_squares:
        locked_squares.remove(current_square)
    else:
        locked_squares.append(current_square)
   
def draw():
    global current_square
    
    current_square = set_current_square() 
