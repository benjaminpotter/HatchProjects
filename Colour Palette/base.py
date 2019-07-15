def setup():
    size(400, 400)
    
def draw_palette():
    noStroke()
    colorMode(HSB)
    for i in range(10):
        fill(i * 24, 255, 255)
        rect(4 + i * 39, 100, 40, 40)
        
def display_colour():
    fill(get(mouseX, mouseY))
    rect(150, 200, 100, 100)
    
def draw():
    background(255, 0, 0)
    draw_palette()
    display_colour()