def setup():
    size(400, 400)
    create_circles()
    
class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = True
        self.colour = random(50, 200)
        
    def draw_circle(self):
        if self.visible:
            fill(self.colour)
            ellipse(self.x, self.y, 20, 20)
    
    def remove_circle(self):
        if dist(mouseX, mouseY, self.x, self.y) < 20:
            self.visible = False
        
array_of_circles = []

def create_circles():
    global array_of_circles
    
    for x in range(1, 20):
        for y in range(1, 20):
            array_of_circles.append(Circle(x * 20, y * 20))
            
def draw():
    global array_of_circles
    
    background(0)
    for i in range(len(array_of_circles)):
        array_of_circles[i].draw_circle()
        array_of_circles[i].remove_circle()