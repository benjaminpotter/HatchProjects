def setup():
    size(400, 400)
    
    strokeWeight(2.5)
    noFill()
    rectMode(CENTER)

    
rotation = 0
def draw():
    global rotation
    
    background(230)
    
    for i in range(20):
        ellipse(200, 200, i * 20, i * 20)
    
    translate(200, 200)
    rotate(radians(rotation))
    rect(0, 0, 280, 280)
    
    rotation += 1