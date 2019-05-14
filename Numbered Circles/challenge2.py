def setup ():
    size(400, 400)
    
    circle_size = 30
    circle_multiplier = 5
    alpha_multiplier = 40
    
    textAlign(CENTER, CENTER)
    
    for i in range(1, 11):
        x = random(0, 400)
        y = random(0, 400)
    
        fill(random(0, 255), random(0, 255), random(0, 255), i * alpha_multiplier)
        ellipse(x, y, circle_size + (i * circle_multiplier), circle_size + (i * circle_multiplier))
    
        fill(0)
        text(i, x, y)