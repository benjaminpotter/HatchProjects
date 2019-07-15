def setup():
    size(400, 400)
    background(221, 194, 150)
    
def draw():
    #background(221, 194, 150)
    
    if mouseX > 200 and mouseY > 200:
        fill(255, 0, 0) 
        ellipse(random(200, 400), random(200, 400), 20, 20)
        
    if mouseX > 200 and mouseY < 200:
        fill(0, 0, 255) 
        ellipse(random(200, 400), random(0, 200), 20, 20)
    
    if mouseX < 200 and mouseY > 200:
        fill(0, 255, 0) 
        ellipse(random(0, 200), random(200, 400), 20, 20)
        
    if mouseX < 200 and mouseY < 200:
        fill(255, 255, 0) 
        ellipse(random(0, 200), random(0, 200), 20, 20)