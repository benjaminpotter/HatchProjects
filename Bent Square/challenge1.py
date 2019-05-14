def setup():
    size(400, 400)
    
    strokeWeight(2.5)
    noFill()

    for i in range(20):
        stroke(random(0, 255),random(0, 255),random(0, 255))
        ellipse(200, 200, i * 20, i * 20)
        
    stroke(0)
    rect(60, 60, 280, 280)