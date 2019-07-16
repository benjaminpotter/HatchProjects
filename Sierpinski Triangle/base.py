point1 = [200,50]
point2 = [350,350]
point3 = [50,350]
selectedPoint = []
currentPoint = [point1[0], point1[1]]

def choosePoint() :
  randomNumber = random(0,3)
  if randomNumber > 0 :
    selectedPoint = point1
  if randomNumber > 1 :
    selectedPoint = point2
  if randomNumber > 2 :
    selectedPoint = point3

def drawPoint() :
  currentPoint[0] += (selectedPoint[0] - currentPoint[0])/2
  currentPoint[1] += (selectedPoint[1] - currentPoint[1])/2
  point(currentPoint[0], currentPoint[1])

background(3,70,200)

def draw():
  stroke(250,167,12)
  choosePoint()
  drawPoint()
