numRows = 10
radius = (400 / numRows) / 2
translateX = radius
translateY = sqrt(3) * radius

def setupDraw():
   background(144, 169, 209)
   strokeWeight(3)
   fill(0, 255, 30)
setupDraw()

def drawTennisBalls():
   for i in range (numRows, 0, -1) :
       fill(random(0, 255), random(0, 255), random(0, 255))
       for j in range (0, i) :
           x = radius * (j * 2 + 1)
           ellipse(x, 400 - radius, radius * 2, radius * 2)
      
   translate(translateX, -translateY)

drawTennisBalls()
