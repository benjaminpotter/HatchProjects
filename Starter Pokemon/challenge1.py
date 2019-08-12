pokeball = getImage("pokemon/ball-closed")
ballPikachu = getImage("pokemon/ball-pikachu")
ballSquirtle = getImage("pokemon/ball-squirtle")
ballBulbasaur = getImage("pokemon/ball-bulbasaur")
posX = 200
posY = 200

imageMode(CENTER)
background(255)
image(pokeball, posX, posY)

def keyPressed():
   global posX, posY, ballBulbasaur, ballSquirtle, ballPikachu, pokeball
   background(255)
   fill(0,0,0)
   textAlign(CENTER)
   textSize(30)
   if key == 'p' :
       image(ballPikachu, posX, posY)
       text("Pikachu", 200, 50)
   if key == 's' :
       image(ballSquirtle, posX, posY)
       text("Squirtle", 200, 50)
   if key == 'b' :
       image(ballBulbasaur, posX, posY)
       text("Bulbasaur", 200, 50)
