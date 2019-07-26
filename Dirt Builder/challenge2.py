img = getImage("minecraft/block-grass")
imageMode(CENTER, CENTER)
widthSize = 0
heightSize = 0

def draw():
   if keyIsPressed and keyCode == UP :
       widthSize = 100
       heightSize = 100
   elif keyIsPressed and keyCode == DOWN :
       widthSize = 30
       heightSize = 30
   elif keyIsPressed and keyCode == RIGHT :
       widthSize = 200
       heightSize = 200
 
   elif keyIsPressed and keyCode == LEFT :
       widthSize = 10
       heightSize = 10
