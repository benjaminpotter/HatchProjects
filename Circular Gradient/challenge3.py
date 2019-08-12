radius = width
circleHue = 0

def drawGradient():
 global radius, circleHue
 circleHue +=1
 for r in range (radius, 0, -r) :
   global r
   fill(circleHue, 90, 90)
   ellipse(200, 200, r, r)
   circleHue = (circleHue + 1) % 360

def draw():
   global radius, circleHue
   colorMode(HSB, 360, 100, 100)
   noStroke()
   frameRate(25)
   background(0)
   drawGradient()
   fill(255)
