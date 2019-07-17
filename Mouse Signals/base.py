 xvals =[width]
 yvals =[width]
 bvals =[width]
def trackSignals = function(){
  xvals[width-1] = mouseX
  yvals[width-1] = mouseY
  if mouseIsPressed :
    bvals[width-1] = 0
  else :
    bvals[width-1] = 255

def moveValues():
    for i in range (1, width) : 
        xvals[i-1] = xvals[i] 
        yvals[i-1] = yvals[i]
        bvals[i-1] = bvals[i]

def drawBackground():
  background(102)
  fill(255)
  noStroke()
  rect(0, height/3, width, height/3+1)

def drawSignals():
  for i in range (1, width) :
    stroke(255)
    point(i, xvals[i]/3)
    stroke(0)
    point(i, height/3+yvals[i]/3)
    stroke(255)
    line(i, 2*height/3+bvals[i]/3, i, (2*height/3+bvals[i-1]/3))

def draw():
  trackSignals()
  moveValues()
  drawBackground()
  drawSignals()
