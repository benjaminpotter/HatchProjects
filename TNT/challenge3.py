img1 = getImage("minecraft/tnt")
img2 = getImage("minecraft/chicken")
imageMode(CENTER, CENTER)
background(100, 100, 100)
image(img1, 200, 200, 200, 200)

def draw():
   x = random(0, 400)
   y = random(0, 400)
   if mousePressed :
   image(img2, x, y, 200, 200)
   
