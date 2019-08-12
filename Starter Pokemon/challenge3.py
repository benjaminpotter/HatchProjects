pokeball = getImage("pokemon/ball-closed")
ballPikachu = getImage("pokemon/ball-pikachu")
ballSquirtle = getImage("pokemon/ball-squirtle")
ballBulbasaur = getImage("pokemon/ball-bulbasaur")

def mouseClicked():
   imageMode(CENTER)
   background(255)
       if mouseX >= 25 and mouseX <= 130 and mouseY >= 143 and mouseY <= 250 :
           image(scyther, 200, 200)
       elif mouseX >= 145 and mouseX <= 253 and mouseY >= 143 and mouseY <= 250 :
           image(pikachu, 200, 200)
       elif mouseX >= 265 and mouseX <= 370 and mouseY >= 143 and mouseY <= 250 :
           image(charmander, 200, 200)
       else :
           image(pokeball, 200, 200, 110, 110)
           image(pokeball, 80, 200, 110, 110)
           image(pokeball, 320, 200, 110, 110)
