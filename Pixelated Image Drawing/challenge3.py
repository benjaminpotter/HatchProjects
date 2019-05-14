def setup():
    size(400, 400)
    
x_pos = 0
y_pos = 0
pixel_size = 40

r = 0
g = 0
b = 0

def draw():
    global x_pos, y_pos, pixel_size
    global r, g, b
    
    if key == 'r':
        r = 255
        g = 0
        b = 0
    elif key == 'g':
        r = 0
        g = 255
        b = 0
    elif key == 'b':
        r = 0
        g = 0
        b = 255
    
    if mousePressed:
        x_pos = floor(mouseX / pixel_size) * pixel_size
        y_pos = floor(mouseY / pixel_size) * pixel_size

        noStroke()
        fill(r, g, b)
        rect(x_pos, y_pos, pixel_size, pixel_size)