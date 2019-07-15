def setup():
    size(400, 400)
    
#spaceShip = getImage("animals/spider")
posY = 0;

def draw():
    global posY#, spaceShip
    
    background(36, 36, 36)
    posY = constrain(mouseY, 0, 300)
    rect(25, posY, posY, posY)
    #image(spaceShip, 25, posY, posY, posY)