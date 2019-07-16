randomNumber = 0;
def setupDrawing() : 
  frameRate(2)
  fill(255)
  textSize(24)
  textAlign(CENTER,0)

setupDrawing()
def displayRandomNumber() :
  randomNumber = random(10)
  text("Random no: "+ randomNumber,200,140)
  text("Rounded: "+ round(randomNumber),200,170)
  text("Rounded down: "+floor(randomNumber),200,200)
  text("Rounded up: "+ ceil(randomNumber),200,230)

def draw() :
  background(0)
  displayRandomNumber()
