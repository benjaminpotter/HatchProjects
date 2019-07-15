def setup():
    size(400, 400)
    
    r = 0
    for count in range(400):
        noStroke()
        
        fill(0, 0, 0)
        rect(0, r, 400, 25)
        
        fill(158, 158, 158)
        rect(70, r, 70, 25)
        rect(260, r + 25, 70, 25)
        
        r += 50