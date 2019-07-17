colourComponent = 255
barX = 0
emergency = False
def drawButton():
    fill(0, 0, 0)
    textSize(30)
    text("In case of emergency \n  press the button!", 60, 70)
    fill(255, 60, 0)
    ellipse(200,230,150,150)
    fill(255, 255, 255)
    textSize(20)
    text("EMERGENCY", 135, 235)
    
def setup():
    size(400,400)

def fadeOut():
    global colourComponent
    colourComponent -=2

def countDown():
    global barX
    barX = barX+2
    if(barX>=250):
        barX=250
  
    fill(255,255,255)
    rect(70, 230, 255, 30)
    fill(255, 0, 0)
    rect(72, 232, barX, 27)
    textSize(30)
    text("Turning off...", 120,180)
  
def mouseClicked():
    global emergency
    if((dist(mouseX, mouseY, 200, 230))<75): 
        emergency=True

def draw():
    global colourComponent
    background(colourComponent)
    if(emergency==False):
        drawButton()
    elif (colourComponent > 0):
        fadeOut()
        countDown()
    else: 
        colourComponent = 0
