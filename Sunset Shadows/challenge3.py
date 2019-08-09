sunPos = 100
sunSpeed = 1

def drawSunset():
   global sunPos, sunSpeed
   noStroke()
   for x in range (400, -50, -5) :
       for y in range (400, -50, -5) :
           fill(x, y, 355 - sunPos)
           ellipse(x, y, 50, 50)
   fill(0, sunPos - 100)
   rect(0, 0, 400, 400)
   fill(255, 300 - sunPos / 2, 0)
   ellipse(200, sunPos, 80, 80)

def drawShadows():
   global sunPos, sunSpeed
   fill(0)
   ellipse(200, 400, 600, 200)
   ellipse(150, 270, 20, 20)
   ellipse(150, 300, 10, 40)
   ellipse(160, 260, 20, 20)
   ellipse(160, 300, 10, 70)

def draw():
   global sunPos, sunSpeed
   background(0)
   drawSunset()
   drawShadows()
   sunPos = sunPos + sunSpeed
