def setup():
    size(400, 400)

pickaxe = getImage("minecraft/pickaxe-diamond")
def draw():
  background(0, 0, 0)
  image(pickaxe, mouseX, mouseY) 