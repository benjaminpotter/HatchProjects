cowList = []
cowImage = getImage("minecraft/cow")
imageMode(CENTER,CENTER)
def cow():
  this.yPos = random(100,350)
  this.xPos = 400
  this.speed = 10
  this.rotation = 2
  this.isRolling = FALSE

def drawBackground() :
  background(198, 255, 246)
  noStroke()
  fill(132, 196, 98)
  rect(0,130,400,400)

def moveCow():
  for i in range(0, cowList.length) :
    cowList[i].xPos -= cowList[i].speed
    cowList[i].rotation -= 5
    translate(cowList[i].xPos, cowList[i].yPos)
    rotate(cowList[i].rotation)
    image(cowImage,0, 0)
    resetMatrix()

def draw():
  drawBackground()
  moveCow()

def mouseClicked():
  cowList.append(new cow())
