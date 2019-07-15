def setup():
    size(400, 400)
 
x = 200
y = 200
angle = 0
speed = 10

def follow_mouse():
    global x, y, angle
    
    if dist(mouseX, mouseY, x, y) > 10:
        angle = atan2(mouseY - y, mouseX - x)
        x += cos(angle) * speed
        y += sin(angle) * speed
        
def draw():
    global x, y
    
    background(0)
    
    follow_mouse()
    ellipse(x, y, 50, 50)