def setup():
    size(400, 400)
    
    strokeWeight(2.5)
    noFill()

    for i in range(20):
        ellipse(200, 200, i * 20, i * 20)
    
    rect(60, 60, 280, 280)