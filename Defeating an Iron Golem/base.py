golemHP = 100
damage = 7
numHits = 0
def displayCalculator():
  background(153, 153, 153)
  textSize(20)
  if golemHP >= 0 :
    text("The Iron Golem has " + golemHP + " HP.", 80, 100)
  else :
    text("You Defeated the Iron Golem in " +numHits+ " hits.", 30, 200)

def hitGolem():
  if golemHP > 0 :
    golemHP -= damage
    numHits +=1

def draw():
  displayCalculator()

def mouseClicked():
  hitGolem()
