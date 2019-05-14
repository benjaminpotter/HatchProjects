def draw ():
    r = 0
    g = 0
    b = 0

    if mouseY > (height / 2): 
        r = 56
        g = 155
        b = 242
    else :
        r = 56
        g = 220
        b = 56

    draw_raindrop(r, g, b)    

def draw_raindrop (r, g, b):
    raindrop_size = map(mouseX, 0, width, 2, 18)

    x = round (random(width))
    y = round (random(height))
    
    fill(r, g, b, 50)
    noStroke()
    ellipse(x, y, raindrop_size, raindrop_size)