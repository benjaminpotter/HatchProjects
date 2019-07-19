character1 = getImage("disney/winnie")
character2 = getImage("disney/eeyore")
imageMode(CENTER)

def draw():
   background(0,130,196)
   image(character1, mouseX, mouseY, 150, 150)
   image(character2, mouseY, mouseX, 150, 150)
