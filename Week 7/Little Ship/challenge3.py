def setup():
    size(400, 400)
    
#spaceShip = getImage("animals/spider")
#puppy = getImage("animals/sleeping-puppy")
posY = 0
posX = 0

def draw():
    global posY, posX#, spaceShip
    
    background(36, 36, 36)
    posY = constrain(mouseY, 0, 300)
    rect(25, posY, posY, posY)
    #image(spaceShip, 25, posY, posY, posY)
    
    posX = constrain(mouseX, 0, 300)
    rect(posX, 25, posX, posX)
    #image(puppy, 25, posX, posX, posX)