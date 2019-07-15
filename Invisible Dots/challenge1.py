def setup():
    size(400, 400)
    global square_size, line_size
    
    background(255)
    noStroke()
    
    for x in range(400):
        for y in range(400):
            fill(100, 150, 200)
            rect(x * square_size, y * square_size, square_size - line_size, square_size - line_size)
    
square_size = 50
line_size = 10