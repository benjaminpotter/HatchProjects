footballSpeed = 10
footballX = 0
def drawScene() :
  background(50, 130, 13)
  fill(235, 247, 5)
  rect(324, 42, 5, 113)
  fill(222, 128, 27)
  ellipse(footballX, 100, 60, 40)
  fill(235, 247, 5)
  rect(337, 176, 8, 80)
  rect(350, 50, 7, 150)
  quad(350, 200, 325, 160, 325, 150, 350, 180)

def kickFootball() :
  footballX += footballSpeed

def draw() :
  drawScene()
  kickFootball()
