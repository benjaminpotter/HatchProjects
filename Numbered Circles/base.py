def setup ():
    size(400, 400)
    
    textAlign(CENTER, CENTER)
    
    for i in range(10):
        x = random(0, 400)
        y = random(0, 400)
    
        fill(random(0, 255), random(0, 255), random(0, 255), random(0, 255))
        ellipse(x, y, 50, 50)
    
        fill(0)
        text(i, x, y)