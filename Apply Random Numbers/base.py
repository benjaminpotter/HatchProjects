def setup():
    size(400, 400)
    
    background(random(0, 255), random(0, 255), random(0, 255))
    
    ellipse(200, 50, random(0, 100), random(0, 100))
    rect(200, 150, random(0, 100),random(0, 100))
    strokeWeight(5)
    line(100, 200, random(200, 400), random(300, 400))
    
    textSize(18)
    fill(random(0, 255), random(0, 255), random(0, 255))
    text("Restart the page to see everything change!", 30, 380)