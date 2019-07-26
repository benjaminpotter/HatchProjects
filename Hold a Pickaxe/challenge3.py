pickaxe = getImage("minecraft/pickaxe-diamond") 
wood = getImage("minecraft/sword-wood")

def draw():
   background(0, 0, 0)
   image(pickaxe, mouseX, mouseY)
   image(wood, mouseY, mouseX)
