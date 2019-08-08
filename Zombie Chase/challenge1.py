zombie = getImage("minecraft/zombie")
steve = getImage("minecraft/steve")
steveSpeed = 4
zombieSpeed = 8
sPos = 150
zPos = 250

def drawCharacters():
   image(steve, sPos, 220, 50, 70)
   image(zombie, zPos, 220, 50, 70)

def moveCharacters():
   sPos -= steveSpeed
   zPos -= zombieSpeed

   if zPos < -50 :
       zPos = 450
   if sPos < -50 :
       sPos = 450

def draw():
   background(128, 187, 231)
   noStroke()
   fill(98, 146, 88)
   rect(0, 250, 400, 400)
   drawCharacters()
