def setup():
    size(400, 400)
    
is_colour_selected = False
selected_colour = None
    
def draw_palette():
    noStroke()
    colorMode(HSB)
    for i in range(10):
        fill(i * 24, 255, 255)
        rect(4 + i * 39, 100, 40, 40)
        
def display_colour():
    fill(get(mouseX, mouseY))
    ellipse(200, 250, 100, 100)
    
def mousePressed():
    global selected_colour, is_colour_selected
    
    if is_colour_selected == False:
        selected_colour = get(mouseX, mouseY)
        if selected_colour == color(255):
            selected_colour = None
        else:
            is_colour_selected = True
            background(255)

def draw_picture():
    if mousePressed:
        ellipse(mouseX, mouseY, 10, 10)
    
def draw():
    global is_colour_selected, selected_colour
    
    if is_colour_selected:
        fill(selected_colour)
        draw_picture()
    else:
        background(255)
        draw_palette()
        display_colour()