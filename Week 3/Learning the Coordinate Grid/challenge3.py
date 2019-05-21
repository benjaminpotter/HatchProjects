def setup():
    size(400, 400)
    
points = []
    
def mouse_point():
    fill(255)
    ellipse(mouseX - 2, mouseY + 2, 2, 2)
    return (mouseX, mouseY)
    
def display_coordinates():
    textSize(14)
    text(str(mouseX) + " , " + str(mouseY), mouseX, mouseY)

def draw_points(points):
    fill(0)
    for p in points:
        ellipse(p[0] - 2, p[1] + 2, 2, 2)
        textSize(14)
        text(str(p[0]) + " , " + str(p[1]), p[0], p[1])
    
def draw():
    global points
    background(100, 150, 200)
    
    draw_points(points)