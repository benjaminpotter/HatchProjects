r = 255
g = 0
b = 0

def mouseDragged ():
    noStroke()
    fill(r, g, b)
    ellipse(mouseX, mouseY, 10, 10)
    
def draw ():
    return