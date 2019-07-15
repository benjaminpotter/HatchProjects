def setup():
    size(400, 400)
    imageMode(CENTER)
    background(255)
    image(pokeball, posX, posY)

pokeball = getImage("pokemon/ball-closed")
ballPikachu = getImage("pokemon/ball-pikachu")
ballSquirtle = getImage("pokemon/ball-squirtle")
ballBulbasaur = getImage("pokemon/ball-bulbasaur")
posX = 200
posY = 200

def keyPressed():
    global posX, posY
    global pokeball, ballPikachu, ballSquirtle, ballBulbasaur
    background(255)
    if key == 'p':    
        image(ballPikachu, posX, posY)
    if key == 's':
        image(ballSquirtle, posX, posY)
    if key == 'b':
        image(ballBulbasaur, posX, posY)