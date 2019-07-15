def setup():
    size(400, 400)

def keyPressed():
    fill(random(0, 255), random(0, 255), random(0, 255))
    random_x = random(50, 350)
    random_y = random(50, 350)
    ellipse(random_x, random_y, 50, 50)
    fill(255)
    textSize(20)
    text(key, random_x - 5, random_y + 5)
    
def draw():
    return