def setup():
    size(400, 400)
    textAlign(CENTER, CENTER)
    
isBroken = False
    
def death_star():
    background(0)
    
    stroke(100)
    strokeWeight(2)
    fill(50)
    ellipse(150, 150, 150, 150)
    ellipse(180, 180, 50, 50)
    
def draw_planet():
    fill(11, 121, 168)
    noStroke()
    ellipse(300, 300, 100, 100)
    
def blow_up():
    fill(255, 131, 0)
    noStroke()
    ellipse(300, 300, 150, 150)
    
def draw():
    global isBroken
    
    death_star()
    
    if isBroken == False:
        draw_planet()
    
    if mousePressed:
        stroke(0, 150, 0, random(255))
        strokeWeight(10)
        line(180, 180, mouseX, mouseY)
        
        if dist(mouseX, mouseY, 300, 300) < 100 and isBroken == False:
            blow_up()
            isBroken = True