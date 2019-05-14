#global variables    
r = 255
g = 0
b = 0

brush_size = 15

def mouseDragged ():
    noStroke()
    fill(r, g, b)
    ellipse(mouseX, mouseY, brush_size, brush_size)
    
def draw ():
    # in python functions create their own 'namespaces' 
    # this means we have to tell the function to use the global 
    # variables instead of ones it creates

    global r 
    global g 
    global b 
    
    if keyPressed:
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