def setup():
    size(400, 400)
    rectMode(CENTER)

speed = 10
x_pos = []
y_pos = []

colour_mode = 0

def store_position():
    global x_pos, y_pos
    
    i = 5
    while i <= 400:
        x_pos.append(i);
        y_pos.append(i);     
        i += 10
        
def keyPressed():
    global colour_mode
    
    if key == 'r':
        colour_mode = 0
    elif key == 'g':
        colour_mode = 1
    elif key == 'b':
        colour_mode = 2
    
def draw_boxes():
    global x_pos, y_pos, speed
          
    noStroke()
    if colour_mode == 0:
        fill(random(0, 255), 0, 0)
    elif colour_mode == 1:
        fill(0, random(0, 255), 0)
    elif colour_mode == 2:
        fill(0, 0, random(0, 255))
    for i in range(speed):
        rect(x_pos[int(random(0, 40))], y_pos[int(random(0, 40))], 10, 10)
        
def draw():
    store_position()
    draw_boxes()