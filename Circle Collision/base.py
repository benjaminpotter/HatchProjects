def setup():
    size(400, 400)

ball_rad = 40
pylon_rad = 20

def draw_ball():
    global ball_rad
    
    strokeWeight(2)
    fill(255)
    ellipse(mouseX, mouseY, ball_rad * 2, ball_rad * 2)
    strokeWeight(1)
    line(mouseX, mouseY, 200, 200)
    
def draw_pylon():
    global pylon_rad
    
    strokeWeight(2) 
    fill(255, 162, 0)
    ellipse(200, 200, pylon_rad * 2, pylon_rad * 2)
    
def check_collision():
    distance = dist(mouseX, mouseY, 200, 200)
    if distance < pylon_rad + ball_rad:
        fill(0)
        textAlign(CENTER, CENTER)
        textSize(50)
        text("Colliding!", 200, 50)
    
def draw():
    background(47, 186, 121)
    
    draw_pylon()
    draw_ball()
    check_collision()