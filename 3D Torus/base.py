def setup():
	size(400, 400)
detail = 40
maxSize = 100
f = 0
noFill()
strokeWeight(2)

def createShape() :
  for i in range (f, 360 + f, 360 / detail) :
    radius = maxSize * (sin(i) + 2)
    offset = cos(i) * 40
    pushMatrix()
    translate(width / 2 + offset, height / 2 - offset, offset)
    rotate(45)
    stroke(max(20 + cos(i) * 120, 0))
    ellipse(0, 0, radius, radius / 2)
    popMatrix()
  f += 0.01

def draw() :
  background(173, 16, 16)
  createShape()
