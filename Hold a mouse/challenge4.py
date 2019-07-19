charString = "disney/winnie"

def draw():
   def mouseClicked():
       if charString == "disney/winnie" :
           charString = "disney/eeyore"
       else :
           charString = "disney/winnie"
           
   background(0,130,196)
   image(getImage(charString), mouseX, mouseY, 150, 150)
