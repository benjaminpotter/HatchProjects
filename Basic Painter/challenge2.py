r = 255
g = 0
b = 0

brush_size = 15

def mouseDragged ():
    noStroke()
    fill(r, g, b)
    ellipse(mouseX, mouseY, brush_size, brush_size)
    
def draw ():
    return