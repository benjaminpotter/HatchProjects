face = 0

def drawStamp ():
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

def drawNeutral ():
   strokeWeight(4)
   fill(255, 255, 0)
   ellipse(70, 320, 100, 100)
   fill(0)
   ellipse(70 - 20, 320 - 10, 15, 15)
   ellipse(70 + 20, 320 - 10, 15, 15)
   noFill()
   arc(70, 320 + 20, 30, 30, 0, 3)


def drawHappy ():
   strokeWeight(4)
   fill(255, 255, 0)
   ellipse(190, 320, 100, 100)
   fill(0)
   ellipse(190 - 20, 320 - 10, 15, 15)
   ellipse(190 + 20, 320 - 10, 15, 15)
   noFill()
   arc(190, 320 + 20, 30, 30, 0, 180)


def drawSad ():
   strokeWeight(4)
   fill(255, 255, 0)
   ellipse(320, 320, 100, 100)
   fill(0)
   ellipse(320 - 20, 320 - 10, 15, 15)
   ellipse(320 + 20, 320 - 10, 15, 15)
   noFill()
   arc(320, 320 + 20, 30, 30, 180, 360)


def mouseClicked (e):
   global face
   if mouseX >= 20 and mouseX <= 115 and mouseY >= 275 and mouseY <= 365 :
           face = 0
           drawStamp()
       
   elif mouseX >= 140 and mouseX <= 240 and mouseY >= 275 and mouseY <= 365 :
           face = 1
           drawStamp()
       
   elif mouseX >= 270 and mouseX <= 370 and mouseY >= 275 and mouseY <= 365 :
           face = 2
           drawStamp()
       
   drawStamp()


def draw ():
   drawNeutral()
   drawSad()
   drawHappy()
