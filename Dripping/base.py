colors = [color(104, 204, 221),color(220, 237, 235),color(36, 106, 150)]
allDots = []
index = 0
noStroke()

def dot() :
 this.x = random(0,400)
 this.y = random(-10,0)
 this.size = random(15,25)
 this.color = colors[round(random(0,colors.length-1))]
 this.speed = random(0,6)
 this.growth = random(0.25,0.75)

def createDot() :
  allDots[index] = new dot()
  index++
  if index > 300 :
    index = 0

def drawDot():
  for i in range (0, allDots.length):
    allDots[i].y += allDots[i].speed
    allDots[i].size -= allDots[i].growth
    fill(allDots[i].color,150)
    ellipse(allDots[i].x,allDots[i].y,allDots[i].size,allDots[i].size);

def draw():
  background(0)
  createDot()
  drawDot()
