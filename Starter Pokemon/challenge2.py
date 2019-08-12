pokeball = getImage("pokemon/ball-closed")
ballPikachu = getImage("pokemon/ball-pikachu")
ballSquirtle = getImage("pokemon/ball-squirtle")
ballBulbasaur = getImage("pokemon/ball-bulbasaur")
mew = getImage("pokemon/mew")
eevee = getImage("pokemon/eevee")
magikarp = getImage("pokemon/magikarp")
posX = 200
posY = 200


imageMode(CENTER)
background(255)
image(pokeball, posX, posY)

def keyPressed():
   global posX, posY, ballBulbasaur, ballSquirtle, ballPikachu, pokeball
   background(255)
   if key == 'p' :
       image(ballPikachu, posX, posY)
   if key == 's' :
       image(ballSquirtle, posX, posY)
   if key == 'b' :
       image(ballBulbasaur, posX, posY)
