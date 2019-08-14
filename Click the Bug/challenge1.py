score = 0
bugX = random(0, 350)
bugY = random(-50, 300)
img = getImage("avatars/mr-pants-pink")

def drawBug():
   image(img, bugX, bugY, 60, 60)

def printScore():
   fill(18, 18, 18)
   text("Score: " + score, 12, 19)

def draw():
   background(232, 255, 224)
   drawBug()
   printScore()

def bugClicked():
   if mouseX < bugX + bugImage.width and mouseX > bugX and mouseY < bugY + bugImage.height and mouseY > bugY :
       score+=1
       bugX = random(0, 350)
       bugY = random(-50, 300)
  

def mouseClicked(e):
   bugClicked()
