def setup ():
    size(400, 400)
    
    circle_size = 30
    circle_multiplier = 5
    
    textAlign(CENTER, CENTER)
    
    for i in range(10):
        x = random(0, 400)
        y = random(0, 400)
    
        fill(random(0, 255), random(0, 255), random(0, 255), random(0, 255))
        ellipse(x, y, circle_size + (i * circle_multiplier), circle_size + (i * circle_multiplier))
    
        fill(0)
        text(i, x, y)