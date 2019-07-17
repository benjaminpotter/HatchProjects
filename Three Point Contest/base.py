numberMade = 0
averageShotPercentage = 31
def drawScene():
  background(59, 103, 191)
  textSize(43)
  text("Three Point Contest" , 30,45)
  textSize(19)
  text("Made: " +numberMade, 76,190)
  text("Missed: " + (25 - numberMade), 221, 190)
  fill(255, 150, 150)
  text("Play" , 190, 315)
  noFill()
  rect(80, 300, 235, 20)

def simulateContest():
  if mouseX>80 and mouseX<315 and mouseY>300 and mouseY<320 :
    for i in range (0, 23) :
      num = random(0,100)
      if num > 0 and num < averageShotPercentage :
        numberMade++

def draw():
  drawScene()

def mouseClicked():
  simulateContest()
