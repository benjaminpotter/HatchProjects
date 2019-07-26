strokeWeight(10)
background(0, 0, 0)
for i in range(0, width): 
    r = random(255)
    x = random(0, width)
    stroke(r, r, r, 100)
    line(i, 0, x, height)
