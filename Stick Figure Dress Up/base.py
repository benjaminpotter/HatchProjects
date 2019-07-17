def drawText() :
  textSize(10)
  text("1 = Add Hat", 10,100)
  text("2 = Add Monocle", 10,110)
  text("3 = Add Cane", 10,120)
  text("4 = Add Dress", 10,130)
  text("0 = Clear", 10,150)

drawText()
def drawPerson() :
  noFill()
  strokeWeight(7)
  ellipse(195,90,105,105)
  line(195,143,195,277)
  line(195,276,160,330)
  line(160,330,210,380)
  line(195,277,195,380)
  line(195,157,135,236)
  line(195,155,255,238)

drawPerson()
def drawHat() :
  fill(0)
  rect(135,0,120,65)
  rect(123,65,140,10)

def drawMono() :
  noFill()
  ellipse(175,90,20,20)
  line(164,90,164,120)

def drawCane() :
  noFill()
  arc(140, 250, 30, 30, 200, 350)
  line(125,245,125,380)

def drawDress() :
  fill(0)
  triangle(195,175,140,390,250,390)

def reset() :
  background(255)
  drawText()
  drawPerson()

def keyPressed() :
  if key == '1' :
    drawHat()
  
  if key == '2' :
    drawMono()
  
  if key == '3' :
    drawCane()
  
  if key == '4' :
    drawDress()
  
  if key == '0' :
    reset()
