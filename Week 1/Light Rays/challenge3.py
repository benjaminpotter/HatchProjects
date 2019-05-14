def setup():
    size(400, 400)
    
def draw():
    background(0)
    
    for i in range(400):
        stroke(random(0, 255), random(0, 255), random(0, 255), 50)
        line(random(0, 400), random(0, 400), mouseX, mouseY)
        