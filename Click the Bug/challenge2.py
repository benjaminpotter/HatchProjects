score = 0
bugX1 = random(0, 350)
bugY1 = random(-50, 300)
bugX2 = random(0, 350)
bugY2 = random(-50, 300)
bugImage = getImage("cute/EnemyBug")

def drawBug():
   image(bugImage, bugX1, bugY1, 51, 127)
   image(bugImage, bugX2, bugY2, 51, 127)

def printScore():
   fill(18, 18, 18)
   text("Score: " + score, 12, 19)

def draw():
   background(232, 255, 224)
   drawBug()
   printScore()

def bugClicked():
   if mouseX < bugX1 + width(bugImage) and mouseX > bugX1 and mouseY < bugY1 + height(bugImage) and mouseY > bugY1 :
       score+=1
       bugY1 = random(-50, 300)
   if mouseX < bugX2 + width(bugImage) and mouseX > bugX2 and mouseY < bugY2 + height(bugImage) and mouseY > bugY2 :
       score+=1
       bugX2 = random(0, 350)
       bugY2 = random(-50, 300)
  

def mouseClicked(e):
   bugClicked()
