star = getImage("cute/Star")
rand = random(5, 20)
def displayInstructions() :
  background(21, 34, 66)
  textSize(40)
  fill(204, 204, 204)
  text("Click to make stars", 35, 175)

displayInstructions()

def drawStars() :
  background(21, 34, 66)
  for i in range (0, rand) :
    image(star, random(0, 350), random(0, 350), 40, 65)
  rand = random(5, 20)

def mouseClicked() :
  drawStars()
