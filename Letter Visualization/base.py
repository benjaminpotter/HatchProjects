quote = "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose."
letters = []
amount = []
letterAdded = False
noStroke()
textAlign(CENTER)
def addLetter(thisLetter):
  global letterAdded
  isMatch = match(thisLetter, "[a-z]")
  if isMatch != None :
    for j in range (0, len(letters)) :
      if thisLetter == letters[j] :
        amount[j] += 1
        letterAdded = True
    
    if letterAdded == False :
      letters.append(thisLetter)
      amount.append(1)
    letterAdded = False

def createArray():
  global quote
  quote = quote.lower()
  for i in range (0, len(quote)):
    thisLetter = quote[i]
    addLetter(thisLetter)

createArray()
def drawCircles():
  for x in range (0, len(letters)):
    fill(random(0,255), random(0,255), random(0,255))
    circleSize = amount[x] * 10
    xPos = random(50,350)
    yPos = random(50,350)
    ellipse(xPos, yPos,circleSize,circleSize)
    fill(255)
    textSize(circleSize/1.2)
    text(letters[x],xPos,yPos+circleSize/4)

drawCircles()
