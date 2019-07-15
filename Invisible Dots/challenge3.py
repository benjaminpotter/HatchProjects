def setup():
    size(400, 400)
    draw_scene()
    
square_size = 50
line_size = 10
circle_pos = (random(400), random(400))

def draw_circle(x, y):
    fill(100, 100, 100, 100)
    ellipse(x, y, 20, 20)

def draw_scene():
    global square_size, line_size
    
    background(255)
    noStroke()
    
    for x in range(400):
        for y in range(400):
            fill(100, 150, 200)
            rect(x * square_size, y * square_size, square_size - line_size, square_size - line_size)

def mousePressed():
    global circle_pos
    
    draw_scene()
    if dist(mouseX, mouseY, circle_pos[0], circle_pos[1]) < 20 / 2:
        circle_pos = (random(400), random(400))
    draw_circle(circle_pos[0], circle_pos[1])
    
def draw():
    return