def drawBody():
   fill(90, 175, 80)
   strokeWeight(5)
   ellipse(200, 225, 100, 200)

def drawHead():
   fill(0, 0, 0)
   ellipse(200, 100, 80, 80)

def draw():
   translate(110, 0)
   drawBody()
   drawHead()
   resetMatrix()
   translate(-110, 0)
   drawBody()
   drawHead()
