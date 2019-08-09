def mousing():
   fill(0, 0, 0)
   rect(0, 0, 400, 250)
   fill(39, 46, 179)
   rect(0, 250, 400, 150)
   image(getImage("avatars/mr-pink"), mouseX, 250, mouseY / 2, mouseY / 2)
   image(getImage("avatars/mr-pink-green"), mouseX + 100, 250, mouseY / 2, mouseY / 2)

def draw():
   mousing()
