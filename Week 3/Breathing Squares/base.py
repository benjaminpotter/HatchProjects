def setup():
    size(400, 400)

rotation = 0
speed = 0.01
squares_on = True

def outer_squares():
    popMatrix()
    fill(102, 179, 164)
    rect(0, 0, 175, 175)
    rect(225, 0, 175, 175)
    rect(0, 225, 175, 175)
    rect(225, 225, 175, 175)

def inner_square():
    global speed, rotation
    
    fill(102, 57, 40)
    translate(200, 200)
    rotation += speed
    rotate(rotation)
    rect(-125, -125, 250, 250)
    
def draw():
    global squares_on
    
    background(255)
    noStroke()
    if squares_on:
        pushMatrix()
    inner_square()
    
    if squares_on:
        outer_squares()
        
def keyPressed():
    global squares_on
    
    if key == ' ' and squares_on == True:
        squares_on = False
    elif key == ' ':
        squares_on = True