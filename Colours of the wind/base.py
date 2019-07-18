leafColors = [color(233, 96, 59), color(227, 50, 217), color(171, 88, 196), color(249, 65, 36)]
leafList = []
maxLeaves = 300
index = 0
class leaf :
  def __init__(self, xPos, yPos, size, ySpeed, xSpeed, color):
      self.xPos = -20
      self.yPos = random(-20,300)
      self.size = random(3,10)
      self.ySpeed = random(-2,2)
      self.xSpeed = random(3,7)
      self.color = leafColors[round(random(0,len(leafColors)-1))]

def drawPocahontas() :
  fill(0,0,0)
  rect(185,207,23,55,20)
  fill(170, 63, 55)
  ellipse(200,220,20,20)
  fill(189, 113, 89)
  rect(193,230,15,55,20)

def drawBackground():
  background(225, 139, 152)
  fill(60, 43, 84)
  beginShape()
  vertex(0,300)
  vertex(250,280)
  vertex(200,370)
  vertex(100,400)
  vertex(0,400)
  endShape(CLOSE)
  drawPocahontas()

def moveLeaf() :
  for i in range (0, len(leafList)):
    leafList[i].yPos += leafList[i].ySpeed
    leafList[i].xPos += leafList[i].xSpeed
    noStroke()
    fill(leafList[i].color)
    ellipse(leafList[i].xPos,leafList[i].yPos,leafList[i].size, leafList[i].size-4)

def resetArray() :
  if index > maxLeaves :
    index = 0

def startLeaf() :
  leafList[index] =  leaf() 
  index+=1

def draw() :
  noStroke()
  drawBackground()
  startLeaf()
  moveLeaf() 
  resetArray()
