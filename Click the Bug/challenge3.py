score = 0
bugX = random(0, 350)
bugY = random(-50, 300)
bugSpeed = 1
bugImage = getImage("cute/EnemyBug")

def drawBug():
   image(bugImage, bugX, bugY, 51, 127)
   bugX = bugX + bugSpeed

def printScore():
   fill(18, 18, 18)
   text("Score: " + score, 12, 19)

def draw():
   background(232, 255, 224)
   drawBug()
   printScore()
   if bugX > 405 :
       background(255, 119, 0)
       fill(255, 255, 255)
       textSize(45)
       textAlign(CENTER)
       text("GAME OVER!", 200, 200)
       
def bugClicked():
   if mouseX < bugX + width(bugImage) and mouseX > bugX and mouseY < bugY + height(bugImage) and mouseY > bugY :
       score+=1
       bugX = random(0, 350)
       bugY = random(-50, 300)

def mouseClicked():
   bugClicked()
