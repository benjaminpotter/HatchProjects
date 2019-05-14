def setup():
    size(400, 400)
    
    strokeWeight(2.5)
    noFill()
    rectMode(CENTER)

    for i in range(20):
        rect(200, 200, i * 20, i * 20)
    
    ellipse(200, 200, 280, 280)