blockHardness = 2
timePerHit = 1.5
timeMultiplier = 1
numberOfBlocks = 1

zombie = getImage("minecraft/zombie")

def blockCalculator():
   numberOfBlocks = round(random(1,10))
   timeToBreak = blockHardness * timePerHit * timeMultiplier * numberOfBlocks
   text("For " + numberOfBlocks + " block(s), it would take " + timeToBreak + " seconds.", 80, 200)

frameRate(0.2)

def drawText():
   text("Wood", 100, 300)
   text("Obsidian", 250, 300)
   if mouseX > 75 and mouseX < 125 and mouseY > 275 and mouseY < 325 :
       blockHardness = 2
       timeMultiplier = 1
   elif mouseX > 225 and mouseX < 275 and mouseY > 275 and mouseY < 325 :
       blockHardness = 50
       timeMultiplier = 3.33

def draw():
   background(0, 0, 0)
   blockCalculator()
   image(zombie, 50, 50, 75, 100)
   drawText()
