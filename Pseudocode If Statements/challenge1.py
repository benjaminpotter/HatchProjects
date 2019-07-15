def setup():
    size(400, 400)
    background(221, 194, 150)
    
def draw():
    #background(221, 194, 150)
    
    fill(random(255), random(255), random(255)) 
    
    if mouseX > 200:
        ellipse(random(0, 400), random(0, 400), 20, 20)
        
    if mouseX < 200:
        rect(random(0, 400), random(0, 400), 20, 20)