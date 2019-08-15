runTime = False
i = 0

def displayText():
   fill(133, 129, 129)
   textSize(20)
   if runTime = True :
       text("Click anywhere to begin", 100, 80)
   else :
       text("Now keep clicking and moving around!", 40, 340)

def changeCharacter():
   if runTime == True :
       if i == 1 :
           image(getImage("cute/CharacterHornGirl"), mouseX - 45, mouseY - 90)
       elif i == 2 :
           image(getImage("cute/CharacterCatGirl"), mouseX - 45, mouseY - 90)
       elif i == 3 :
           image(getImage("cute/CharacterPinkGirl"), mouseX - 45, mouseY - 90)
       elif i == 4 :
           image(getImage("cute/CharacterBoy"), mouseX - 45, mouseY - 90)
       elif i == 5 :
           image(getImage("cute/CharacterPrincessGirl"), mouseX - 45, mouseY - 90)
       elif i == 6 :
           image(getImage("avatars/mr-pink"), mouseX - 45, mouseY - 90)
       elif i == 7 :
           image(getImage("avatars/mr-pink-green"), mouseX - 45, mouseY - 90)
       elif i == 8 :
           image(getImage("avatars/mr-pants-orange"), mouseX - 45, mouseY - 90)
       
def draw():
   background(230, 223, 223)
   displayText()
   changeCharacter()


def mouseClicked():
   runTime = True
   i = round(random(1, 8))
