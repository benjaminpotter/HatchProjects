def drawStamp():
   stroke(255, 255, 255)
   strokeWeight(5)
   line(mouseX, mouseY, mouseX + 50, mouseY + 50)
   line(mouseX + 50, mouseY, mouseX, mouseY + 50)

background(20)

def mouseClicked(e):
   drawStamp()
