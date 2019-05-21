def setup():
    size(400, 400)
    
def mouse_point():
    fill(0)
    ellipse(mouseX - 2, mouseY + 2, 2, 2)
    
def display_coordinates():
    textSize(14)
    text(str(mouseX) + " , " + str(mouseY), mouseX, mouseY)
    
def draw():
    background(100, 150, 200)
    
    mouse_point()
    display_coordinates()