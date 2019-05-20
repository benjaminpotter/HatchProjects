def setup():
    size(400, 400)
    textAlign(CENTER, CENTER)
    
def death_star():
    background(0)
    
    stroke(100)
    strokeWeight(2)
    fill(50)
    ellipse(150, 150, 150, 150)
    ellipse(180, 180, 50, 50)
    
def draw():
    death_star()
    
    if mousePressed:
        stroke(0, 150, 0, random(255))
        strokeWeight(10)
        line(180, 180, mouseX, mouseY)
    
    textSize(20)
    fill(160, 249, 112)
    text('May the force be with you.', 200, 300)