def setup():
    size(400, 400)
    background(255)
    create_palette()
    
is_colour_selected = False
selected_colour = 0

palette = []
    
def create_palette():
    global palette
    
    noStroke()
    colorMode(HSB)
    for i in range(10):
        palette.append(color(i * 24, 255, 255))
    
def draw_current_colour():
    global palette, selected_colour
    fill(palette[selected_colour])
    rect(20, 20, 20, 20)
    
def keyPressed():
    global selected_colour
    if keyCode == LEFT:
        if selected_colour + 1 > 9:
            selected_colour = 0
        else:
            selected_colour += 1
    elif keyCode == RIGHT:
        if selected_colour - 1 < 0:
            selected_colour = 9
        else:
            selected_colour -= 1
            
def draw():
    global selected_colour, palette
    
    if mousePressed:
        fill(palette[selected_colour])
        ellipse(mouseX, mouseY, 10, 10)
    
    draw_current_colour()