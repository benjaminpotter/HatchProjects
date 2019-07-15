def setup():
    size(400, 400)
    
def draw_shapes():
    fill(0)
    ellipse(50, 50, 10, 10)
    noFill()
    rect(0, 0, 400, 400)
    
def draw():
    background(181, 215, 224)
    draw_shapes()
    
def keyPressed():
    if keyCode == DOWN:
        scale(0.5)
    elif keyCode == UP:
        scale(1.5)