def setup():
    size(400, 400)
    
def draw():
    fill(255, 0, 0, 10)
    ellipse(400 - mouseX, 400 - mouseY, 200, 200)
    
    fill(0, 255, 0, 10)
    ellipse(mouseX, mouseY, 200, 200)