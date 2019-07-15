def setup():
	size(400, 400)
jerseyColor1 = color(255, 255, 255)
jerseyColor2 = color(158, 153, 9)
name = "Crosby"
number = 87
def drawJersey() 
  fill(jerseyColor1)
  rect(100, 50, 200, 300)
  rect(50, 125, 50, 175)
  rect(300, 125, 50, 175)
  arc(101, 130, 100, 160, 180, 270)
  arc(300, 130, 100, 160, 270, 360)

drawJersey()

def drawJerseyDetails() :
  fill(jerseyColor2)
  rect(100, 250, 200, 20)
  rect(100, 281, 200, 20)
  rect(50, 150, 50, 20)
  rect(300, 150, 50, 20)

drawJerseyDetails()

def printName() :
  textSize(100)
  text(number, 150, 226)
  textSize(30)
  text(name, width / 2 - name.length * 8, 100)

printName()
