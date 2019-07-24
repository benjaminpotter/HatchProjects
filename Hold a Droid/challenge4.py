charString = "starwars/c3po"
imageMode(CENTER)
def draw():
   def mouseClicked():
       if charString == "starwars/c3po" :
           charString = "starwars/yoda"
       else :
           charString = "starwars/c3po"
           
   background(0,130,196)
   image(getImage(charString), mouseX, mouseY, 100, 100)
