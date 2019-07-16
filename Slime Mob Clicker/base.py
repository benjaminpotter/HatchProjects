numOfSlimeKilled = 0;
levelNumber = 1;
xp = 0;
levelMultiplier = 7;
def calculateLevel() :
  if xp >= levelMultiplier * levelNumber :
    levelNumber ++
    levelMultiplier++

def displayCalculator() :
  background(53, 117, 11)
  textSize(15)
  text ("You killed "+ numOfSlimeKilled +" large slime mobs", 100,200)
  textSize(40)
  text("You are level: " + (levelNumber - 1), 60, 300)
  textSize(30)
  text("And you have " + xp + " XP", 70, 350)

def draw() :
    calculateLevel()
  displayCalculator()

def mouseClicked() :
  numOfSlimeKilled ++
  xp += 4
