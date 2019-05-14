def setup():
    size(400, 400)
    
x_pos = 0
y_pos = 0
pixel_size = 20

def draw():
    global x_pos, y_pos, pixel_size
    
    if mousePressed:
        x_pos = floor(mouseX / pixel_size) * pixel_size
        y_pos = floor(mouseY / pixel_size) * pixel_size
        
        noStroke()
        fill(0)
        rect(x_pos, y_pos, pixel_size, pixel_size)