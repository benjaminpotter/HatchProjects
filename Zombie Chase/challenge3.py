zombie = getImage("minecraft/zombie")
steve = getImage("minecraft/steve")
steveSpeed = 4
zombieSpeed = 4
sPos = 150
zPos = 350

def drawCharacters():
   image(steve, sPos, 220, 50, 70)
   image(zombie, zPos, 220, 50, 70)

def moveCharacters():
   zPos -= zombieSpeed

   if zPos < -50 :
       zPos = 450
 
   if keyIsPressed and keyCode == RIGHT :
       sPos += steveSpeed
 
   if keyIsPressed and keyCode == LEFT :
       sPos -= steveSpeed
 
   if sPos > 450 :
       sPos = -50
 
   if sPos < -50 :
       sPos = 450
 

def draw():
   background(128, 187, 231)
   noStroke()
   fill(98, 146, 88)
   rect(0, 250, 400, 400)
   drawCharacters()
   moveCharacters()
   if sPos - zPos > -20 :
       zombieSpeed = 0
       sPos = zPos
       textAlign(CENTER)
       textSize(40)
       fill(255, 0, 0)
       text("Game Over", 200, 150)
