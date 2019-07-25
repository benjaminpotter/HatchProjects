noStroke()
def drawBody(): 
   fill(132, 82, 44)
   rect(100, 123, 200, 200)
   arc(200, 125, 200, 200, 180, 360)

def drawFace(): 
   fill(204, 33, 81)
   ellipse(200, 152, 75, 50)
   fill(0, 0, 0)
   ellipse(165, 90, 10, 58)
   ellipse(235, 90, 10, 58)
   fill(194, 184, 184)
   ellipse(165, 70, 6, 13)
   ellipse(235, 70, 6, 13)
   ellipse(188, 143, 33, 24)

def draw(): 
   drawBody()
   drawFace()
   translate(-150,50)
   drawBody()
   drawFace()
   resetMatrix()
   translate(150,20)
   drawBody()
   drawFace()
   resetMatrix()
   image(getImage("cute/GrassBlock"), 0, 200, 400, 177)
