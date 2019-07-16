lineSize = 20
numOfLines = 80
def drawLines() :
  stroke(255)
  translate(width/2,height/2)
  for i in range (1, numOfLines + 1) :
    rotate(360/numOfLines)
    line(0,0,0,lineSize)

def changeLines() :
  if mouseIsPressed == TRUE && lineSize < 200 :
    lineSize++
  else :
    if lineSize > 20 :
      lineSize--

def draw() :
  background(0)
  changeLines()
  drawLines()
