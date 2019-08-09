def mousing ():
   fill(0, 0, 0)
   rect(0, 0, 400, 250)
   fill(39, 46, 179)
   rect(0, 250, 400, 150)
   image(getImage("avatars/mr-pink"), mouseX, 250, mouseY / 2, mouseY / 2)

def drawBackground ():
   fill(192, 192, 192)
   rect(0, 100, 200, 150)
   rect(200, 50, 100, 200)
   rect(300, 75, 100, 175)
   fill(255, 255, 0)
   rect(20, 120, 30, 40)
   rect(90, 130, 60, 20)
   rect(220, 70, 30, 80)
   rect(320, 105, 30, 30)
   rect(360, 150, 30, 30)

def draw ():
   mousing()
   drawBackground()
