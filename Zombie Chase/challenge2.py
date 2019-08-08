zombie = getImage("minecraft/zombie")
steve = getImage("minecraft/steve")
steveSpeed = 4
zombieSpeed = 4
sPos = 150
zPos = 250

def drawCharacters() :
   image(steve, sPos, 220, 50, 70)
   image(zombie, zPos, 220, 50, 70)

def moveCharacters() :
   zPos -= zombieSpeed

   if zPos < -50 :
       zPos = 450
  
   if keyIsPressed && keyCode === RIGHT :
       sPos += steveSpeed
  
   if keyIsPressed && keyCode === LEFT :
       sPos -= steveSpeed
  
   if sPos > 450 :
       sPos = -50
  
   if sPos < -50 :
       sPos = 450

def draw() :
   background(128, 187, 231)
   noStroke()
   fill(98, 146, 88)
   rect(0, 250, 400, 400)
   drawCharacters()
   moveCharacters()
