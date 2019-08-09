img = getImage("space/rocketship")

def drawSunset():
   noStroke()
   for x in range (400, -50,-5) :
       for y in range (400, -50,-5) :
           fill(x, y, 51)
           ellipse(x, y, 50, 50)
drawSunset()

def drawShadows():
   fill(0)
   ellipse(200, 400, 600, 200)
   ellipse(150, 270, 20, 20)
   ellipse(150, 300, 10, 40)
   ellipse(160, 260, 20, 20)
   ellipse(160, 300, 10, 70)
   tint(0, 0, 0)
   image(img, 200, 100, 100, 100)
drawShadows()
