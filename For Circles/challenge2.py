def setup ():
    size(400, 400)
    
    for i in range(400):
        fill(random(0, 255), random(0, 255), random(0, 255), random(0, 255))
        rect(random(0,400), random(0, 400), 50, 50)