def setup():
	size(400, 400)
numHits = 0
numStrikeouts = 0
battingAverage = 0
def displayStats() :
  textAlign(CENTER, CENTER)
  textSize(40)
  fill(0, 0, 0)
  text("John Doe", 200, 50)
  text(numHits + "\nHits", 100, 200)
  text(numStrikeouts + "\nStrikeouts", 300, 200)
  textSize(30)
  text("Batting Average: " + battingAverage.toFixed(3), 200, 325)

def updateStats() :
  if mouseX < 200 :
    numHits++
  else :
    numStrikeouts++

  battingAverage = numHits / (numStrikeouts + numHits)
  battingAverage = round(battingAverage * 1000) * 0.001

def mouseClicked() :
  updateStats()

def draw() :
 background(66, 179, 0)
 displayStats()
