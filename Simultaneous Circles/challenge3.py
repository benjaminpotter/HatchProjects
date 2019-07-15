def setup():
    size(400, 400)
    rectMode(CENTER)

max_distance = 400

def paint_circles():
    global max_distance
    
    x = -1
    while x < width:
        y = -1
        while y < height:
            circle_size = dist(mouseX, mouseY, x, y)
            circle_size = (circle_size/max_distance) * 66
            fill(255)
            rect(x, y, circle_size, circle_size)
            y += 20
        x += 20
        
def draw():
    background(100, 150, 200)
    
    noStroke()
    paint_circles()