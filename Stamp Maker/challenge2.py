face = 0

def drawStamp():
   global face
   if face == 0 :
       strokeWeight(4)
       fill(255, 255, 0)
       ellipse(mouseX, mouseY, 100, 100)
       fill(0)
       ellipse(mouseX - 20, mouseY - 10, 15, 15)
       ellipse(mouseX + 20, mouseY - 10, 15, 15)
       noFill()
       arc(mouseX, mouseY + 20, 30, 30, 0, 3)
   if face == 1 :
       strokeWeight(4)
       fill(255, 255, 0)
       ellipse(mouseX, mouseY, 100, 100)
       fill(0)
       ellipse(mouseX - 20, mouseY - 10, 15, 15)
       ellipse(mouseX + 20, mouseY - 10, 15, 15)
       noFill()
       arc(mouseX, mouseY + 20, 30, 30, 0, 180)
   if face == 2 :
       strokeWeight(4)
       fill(255, 255, 0)
       ellipse(mouseX, mouseY, 100, 100)
       fill(0)
       ellipse(mouseX - 20, mouseY - 10, 15, 15)
       ellipse(mouseX + 20, mouseY - 10, 15, 15)
       noFill()
       arc(mouseX, mouseY + 20, 30, 30, 180, 360)
       
background(20)

def mouseClicked(w):
  global face
  face = random(0, 2)
  face = round(face)
  drawStamp()
