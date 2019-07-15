def setup():
    size(400, 400)
    
def draw():
    fill(150, 10, 0, 10)
    ellipse(400 - mouseX, 400 - mouseY, 200, 200)
    
    fill(70, 30, 200, 10)
    ellipse(mouseX, mouseY, 200, 200)
    
    fill(70, 30, 200, 10)
    ellipse(mouseX, 400 - mouseY, 200, 200)