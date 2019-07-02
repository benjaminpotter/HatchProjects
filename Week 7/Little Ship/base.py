def setup():
    size(400, 400)
    
#spaceShip = getImage("space/beetleship")
posY = 0;

def draw():
    global posY#, spaceShip
    
    background(36, 36, 36)
    posY = constrain(mouseY, 0, 300)
    rect(25, posY, 100, 100)
    #image(spaceShip, 25, posY, 100, 100)