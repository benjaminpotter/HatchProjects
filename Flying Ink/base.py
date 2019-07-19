allDots = []
colors = []
growth = 0.25
index = 0
noStroke()
class theColor :
    def __init__(self) :
        self.r = 0
        self.g = 0
        self.b = 0

colors.append(theColor())
colors.append(theColor())
class dot :
  def __init__(self, dotColor) :
    self.x = 0
    self.y = 0
    self.speed = 0.5
    self.angle = random(1,360)
    self.size = random(1,3)
    self.color = dotColor

def drawDots () :
  global index
  newColor = color(colors[1].r,colors[1].g,colors[1].b)
  allDots.append(dot(newColor))
  index+=1
  if index > 500 :
    index = 0

def changeColor () :
  colors[0].r = random(0,255)
  colors[0].g = random(0,255)
  colors[0].b = random(0,255)

def fadeColor () :
  if colors[0].r < colors[1].r :
    colors[1].r-=1
 
  if colors[0].r > colors[1].r :
    colors[1].r+=1
 
  if colors[0].g < colors[1].g :
    colors[1].g-=1
 
  if colors[0].g > colors[1].g :
    colors[1].g+=1
 
  if colors[0].b < colors[1].b :
    colors[1].b-=1
 
  if colors[0].b > colors[1].b :
    colors[1].b+=1
 
def moveDots () :
  for i in range (0, len(allDots)) :
    translate(200,200)
    rotate(allDots[i].angle)
    allDots[i].x += allDots[i].speed
    allDots[i].y += allDots[i].speed
    allDots[i].size += growth
    fill(allDots[i].color)
    ellipse(allDots[i].x,allDots[i].y,allDots[i].size,allDots[i].size)
    resetMatrix()
 
def draw () :
  background(255)
  drawDots()
  moveDots()
  fadeColor()
  
def mouseClicked () :
  changeColor()
