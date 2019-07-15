def setup():
    size(400, 400)

class Algae:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        
many_algae = []
algae_size = 10
test = 10
clicked = False
counter = 0

def draw_algae():
    global algae_size
    
    noStroke()
    for a in many_algae:
        fill(a.color)
        rect(a.x, a.y, algae_size, algae_size)
        
def check_position(x, y):
    for a in many_algae:
        if a.x == x and a.y == y:
            return True
        
    return False

def grow_algae():
    global test, algae_size, many_algae
    
    for a in many_algae:
        if random(0, test) < 1:
            dir_x = round(random(-1, 1))
            dir_y = round(random(-1, 1))
            
            x = a.x + (dir_x * algae_size)
            y = a.y + (dir_y * algae_size)
            
            if check_position(x, y) == False:
                many_algae.append(Algae(x, y, color(51, random(120, 180), 130)))
                
def draw():
    global counter, clicked
    
    if counter < 1000 and clicked == True:
        draw_algae()
        grow_algae()
        counter += 1
        
def mousePressed():
    global clicked, counter, many_algae
    
    if clicked == False:
        counter = 0
        clicked = True
        many_algae.append(Algae(mouseX,mouseY,color(51,random(120,180),130)))
        