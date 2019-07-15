def setup():
    size(400, 400)
    noStroke()
    
radius = 0
colour = color(random(255), random(255), random(255))

def draw():
    global radius, colour
    
    fill(0, 10)
    rect(0, 0, 400, 400)
    
    for i in range (1, 40):
        resetMatrix()
        translate(200, 200)
        rotate(i * random(15, 20))
        fill(colour)
        ellipse(radius, radius, radius/8, radius/8)
        radius += 0.3
        
def mousePressed():
    global colour, radius
    
    radius = 0
    background(255)
    colour = color(random(255), random(255), random(255))