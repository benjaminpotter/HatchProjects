def mouseClicked():
background(0)
strokeWeight(10)
for i in range (0, width) :
   r = random(0, 255)
   x = random (0, width)
   stroke(r, r, r, 100)
   line(i, 0, x, height)
