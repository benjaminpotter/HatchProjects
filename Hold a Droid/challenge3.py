imageMode(CENTER)
def draw():
   background(0, 0, 0)
   image(getImage("starwars/c3po"), mouseX, mouseY, 100, 100)
   image(getImage("starwars/yoda"), mouseY, mouseX, 100, 100)
