rolling = FALSE
numberOne = round(random(1,6))
numberTwo = round(random(1,6))

def drawDice():
  fill(255, 255, 255)
  rect(75, 150, 100, 100, 9)
  rect(225, 150, 100, 100, 9)
  fill(0, 0, 0)
  textSize(89)
  text(numberOne, 100, 229)
  text(numberTwo, 248, 229)

def rollDice():
  if rolling :
    numberOne = round(random(1,6))
    numberTwo = round(random(1,6))

def draw() :
  background(255, 230, 219)
  drawDice()
  rollDice()

def mouseClicked():
  rolling = !rolling
