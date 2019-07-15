def setup():
    size(400, 400)
    loadPixels()
    
isFading = False
background_alpha = 0
def draw():
    global background_alpha, isFading
    
    for i in range(width * height):
        pixels[i] = color(random(255))
        
    if background_alpha > 255:
        isFading = True
    elif background_alpha <= 0:
        isFading = False
    
    if isFading:
        background_alpha -= 5
    else:
        background_alpha += 5
        
    print background_alpha
    print isFading
        
    updatePixels()
    
    fill(0, 0, 0, background_alpha)
    rect(0, 0, 400, 400)