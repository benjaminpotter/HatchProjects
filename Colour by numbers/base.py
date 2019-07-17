mode = "none"
paintColor = color(255)
skyColor = color(255)
 roofColor = color(255)
 houseColor = color(255)
 groundColor = color(255)
def drawNumbers() :
 textSize(20)
 fill(0)
 text("1",40,45)
 text("2",195,70)
 text("3",195,200)
 text("4",300,335)

def setColor() :
  if mode == '1' :
    skyColor = paintColor
   
  if mode == '2' :
    roofColor = paintColor
   
  if mode == '3' :
    houseColor = paintColor
   
  if mode == '4' :
    groundColor = paintColor
  

def drawShapes() :
  setColor()
  fill(skyColor)
  rect(0,0,400,400) //sky
  fill(groundColor)
  rect(-1,300,401,100) //ground
  fill(houseColor)
  rect(100,100,200,200) //house
  fill(roofColor)
  triangle(100,100,200,5,300,100) //roof
 
def drawColors() :
  rect(0, 350,400,50)
  fill(230,147,111)
  rect(0,355,100,50)
  fill(179,107,106)
  rect(100,355,100,50)
  fill(158,188,159)
  rect(200,355,100,50)
  fill(181,230,158)
  rect(300,355,100,50)
 
def keyPressed() :
  mode = key

def mouseClicked() :
  paintColor = get(mouseX, mouseY)  
 
def draw() :
  drawShapes()
  drawNumbers()
  drawColors()
 
