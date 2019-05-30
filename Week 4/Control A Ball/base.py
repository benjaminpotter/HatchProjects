def setup():
    size(400, 400)
   
xv = 0
yv = 0
xPos = 200
yPos = 200
speed = 0.5

def draw_ball():
    global xPos, yPos
    
    background(71, 67, 67, 80)
    fill(255)
    ellipse(xPos, yPos, 30, 30)
    
def update_ball():
    global xv, yv, speed, xPos, yPos
    
    if keyPressed:
        if keyCode == UP:
            yv -= speed
        if keyCode == DOWN:
            yv += speed
        if keyCode == LEFT:
            xv -= speed
        if keyCode == RIGHT:
            xv += speed
            
    xv *= 0.95
    yv *= 0.95
    
    xPos += xv
    yPos += yv

def draw():
    draw_ball()
    update_ball()