pos = []
frameCounter = 0

def drawHeart():
   fill(255, 0, 0)
   noStroke()
   triangle(200, 300, 102, 207, 303, 202)
   ellipse(149, 183, 110, 90)
   ellipse(251, 183, 110, 90)
   ellipse(200, 200, 20, 20)

def floatingHearts():
   for i in range (0, 10) :
       if pos[i] == None:
           pos[i] = random(0, 350)
       resetMatrix()
       translate(pos[i], (pos[i + 1]) + (sin(frameCounter + pos[i]) * 4))
       scale(i / 10, i / 10)
       drawHeart()
   frameCounter += 0.1

def draw():
   background(0, 0, 0)
   floatingHearts()
