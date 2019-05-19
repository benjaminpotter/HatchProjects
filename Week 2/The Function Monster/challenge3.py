def setup():
    size(400, 400)
    rectMode(CENTER)
    
    draw_body()
    draw_eye(150, 50)
    draw_eye(250, 50)
    draw_eye(200, 130)
    draw_smile()
    draw_tongue()
    
def draw_body():
    fill(152, 234, 175)
    ellipse(200, 200, 300, 300)
    
def draw_eye(x, y):
    fill(255)
    ellipse(x, y, 80, 80)
    
    fill(0)
    ellipse(x, y, 20, 20)

def draw_smile():
    fill(0)
    arc(200, 250, 100, 100, 0, PI)
    
def draw_tongue():
    noStroke()
    fill(255, 100, 100)
    rect(200, 290, 70, 30)
    arc(200, 300, 70, 30, 0, PI)