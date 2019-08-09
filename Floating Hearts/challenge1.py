pos = []
pic = getImage("cute/Star")
frameCounter = 0

def floatingStars():
   for i in range (0, 10) :
       if pos[i] == False :
           pos[i] = random(50, 350)
       resetMatrix()
       translate(pos[i], (pos[i + 1]) + (sin(frameCounter + pos[i]) * 4))
       scale(i / 10, i / 10)
       image(pic, 0, 0)
   frameCounter += 0.1

def draw():
   background(0, 0, 0)
   floatingStars()
