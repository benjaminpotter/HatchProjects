windowY = 200
scenery = loadImage("/static/images/processingJS/avatars/aqualine-sapling.png")
def drawWindow():
  fill(255, 255, 255, 80)
  stroke(255,255,255)
  strokeWeight(5)
  rect(58,28,300,340)
  image(scenery, 140,210,150,150)
  rect(58, 30, 300, 170)
  rect(58, windowY, 300, 170)
def draw(): 
  background(70)
  drawWindow()

def mouseMoved(e): 
    global windowY
    if mouseX>50 and mouseX<350:
        windowY=mouseY
    if windowY > 200:
        windowY = 200
    if windowY < 30:
        windowY = 30
        
