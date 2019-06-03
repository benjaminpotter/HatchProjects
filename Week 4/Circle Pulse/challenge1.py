def setup():
    size(400, 400)

colour_comp = 255
delta_colour = 9
x = 0
y = 0
go = False

def pulse():
    global colour_comp, delta_colour, x, y, go

    fill(colour_comp)
    ellipse(x, y, 100 - (colour_comp * 0.1), 100 - (colour_comp * 0.1))
    colour_comp -= delta_colour
    
    if colour_comp <= 0:
        go = False
        colour_comp = 255
        
def draw():
    global go
    
    background(0)
    noStroke()
    if go == True:
        pulse()

def keyPressed():
    global x, y
    global go
    
    x = mouseX
    y = mouseY
    go = True