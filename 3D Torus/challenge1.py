detail = 40
maxSize = 100
f = 0
noFill()
strokeWeight(2)

def createShape():
   for i in range (int(f), int(360 + f), int(360 / detail)) :
       radius = maxSize * (sin(i) + 2)
       offset = cos(i) * 40
       push()
       translate(width / 2 + offset, height / 2 - offset, offset)
       rotate(45)
       stroke(max(20 + cos(i) * 120, 0))
       ellipse(0, 0, radius, radius / 2)
       pop()
   global f
   f += 0.01

def draw():
   background(173, 16, 173)
   createShape()
