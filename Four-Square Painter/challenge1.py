def fourSquareOutline():
   strokeWeight(5)
   line(133, 0, 133, 400)
   line(266, 0, 266, 400)
   line(0, 133, 400, 133)
   line(0, 266, 400, 266)
fourSquareOutline()

def setRandomColour():
   fill(random(0, 255), random(0, 255), random(0, 255))
   
def drawSquare():
   if mouseX < 133 and mouseY < 133 :
       rect(0, 0, 133, 133)
   elif mouseX > 133 and mouseX < 266 and mouseY < 133 :
       rect(133, 0, 133, 133)
   elif mouseX > 266 and mouseY < 133 :
       rect(266, 0, 133, 133)
   elif mouseX < 133 and mouseY > 133 and mouseY < 266 :
       rect(0, 133, 133, 133)
   elif mouseX > 133 and mouseX < 266 and mouseY > 133 and mouseY < 266 :
       rect(133, 133, 133, 133)
   elif mouseX > 266 and mouseY > 133 and mouseY < 266 :
       rect(266, 133, 133, 133)
   elif mouseX < 133 and mouseY > 266 :
       rect(0, 266, 133, 133)
   elif mouseX > 133 and mouseX < 266 and mouseY > 266 :
       rect(133, 266, 133, 133)
   elif mouseX > 266 and mouseY > 266 :
       rect(266, 266, 133, 133)

def mouseClicked(e):
   setRandomColour()
   drawSquare()
