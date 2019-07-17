strokeColor = color(0, 0, 0)
def drawPallete():
    fill(66, 112, 204)
    rect(300,360,80,35)
    fill(255, 255, 255)
    textSize(11)
    text("RANDOM \n COLOR", 315, 375)
    fill(255, 0, 0)
    rect(40, 360, 30, 30)
    fill(0, 255, 0)
    rect(90, 360, 30, 30)
    fill(0, 0, 255)
    rect(140, 360, 30, 30)
    fill(255, 255, 0)
    rect(190, 360, 30, 30)
    fill(255, 0, 255)
    fill(255, 0, 255)
    rect(240, 360, 30, 30)

  
def setup():
    global noStroke
    global drawPalette
    size(400,400)
    noStroke()
    drawPallete()
    
def draw():
    return
    

def paintPixels():
    if(mouseY > 50 and mouseY < 360):
        global strokeColor
        strokeWeight(5)
        stroke(strokeColor)
        point(mouseX, mouseY)
  

def selectColour():
    global strokeColor
    if (mouseY > 360 and mouseY < 395):
        if(mouseX > 300 and mouseX < 380 ):
            strokeColor = color(random(0,191), random(0,191), random(0,191))
        elif(mouseX > 40 and mouseX < 70) :
            strokeColor = color(255, 0, 0)
        elif(mouseX > 90 and mouseX < 120):
            strokeColor = color(0, 255, 0)
        elif(mouseX > 140 and mouseX < 170): 
            strokeColor = color(0, 0, 255)
        elif(mouseX > 190 and mouseX < 210): 
            strokeColor = color(255, 255, 0)
        elif(mouseX > 240 and mouseX < 270): 
            strokeColor = color(255, 0, 255)
    
  

def mouseDragged(): 
    paintPixels()

def mouseClicked():
    selectColour()
