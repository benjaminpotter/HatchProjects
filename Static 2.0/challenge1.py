def setup():
    size(400, 400)
    loadPixels()
    
def draw():
    for i in range(width * height):
        pixels[i] = color(random(255), random(255), random(255))
        
    updatePixels()