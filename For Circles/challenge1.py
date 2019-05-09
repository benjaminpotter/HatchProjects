def setup ():
    size(400, 400)
    
    for i in range(400):
        fill(0, 0, random(0, 255), random(0, 255))
        ellipse(random(0,400), random(0, 400), 50, 50)