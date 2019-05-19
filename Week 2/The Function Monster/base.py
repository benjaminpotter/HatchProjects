def setup():
    size(400, 400)
    
    draw_body()
    draw_eye(150, 50)
    draw_eye(250, 50)
    
def draw_body():
    fill(152, 234, 175)
    ellipse(200, 200, 300, 300)
    
def draw_eye(x, y):
    fill(255)
    ellipse(x, y, 80, 80)
    
    fill(0)
    ellipse(x, y, 20, 20)
    