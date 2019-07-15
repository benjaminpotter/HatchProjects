circle_size1 = 1
circle_size2 = 1

circle_speed1 = random(1, 5)
circle_speed2 = random(1, 5)

def setup():
    size(400, 400)

def draw():
    global circle_size1, circle_size2, circle_speed1, circle_speed2
    
    background(255)
    
    ellipse(200, 200, circle_size1, circle_size1)
    ellipse(200, 200, circle_size2, circle_size2)

def mouseClicked():
    global circle_size1, circle_size2, circle_speed1, circle_speed2
    
    circle_size1 += circle_speed1
    circle_size2 += circle_speed2
