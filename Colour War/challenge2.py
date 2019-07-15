def setup():
    size(400, 400)
    rectMode(CENTER)

speed = 10
x_pos = []
y_pos = []

def store_position():
    global x_pos, y_pos
    
    i = 5
    while i <= 400:
        x_pos.append(i);
        y_pos.append(i);     
        i += 10
    
def draw_boxes():
    global x_pos, y_pos, speed
          
    noStroke()
    fill(0, 0, random(0, 255))
    for i in range(speed):
        x = x_pos[int(random(0, 40))]
        if x > 200:
            rect(x, y_pos[int(random(0, 40))], 10, 10)
        else:
            ellipse(x, y_pos[int(random(0, 40))], 10, 10)
        
def draw():
    store_position()
    draw_boxes()