sword = ["Wooden", "Golden", "Stone", "Iron", "Diamond"]
durability = [60, 33, 132, 251, 1562]
chosenSword = 0
swordDamage = durability[chosenSword]
hitBar = 200
def calculateHitBar():
  hitBar = map(swordDamage, 0, durability[chosenSword], 0, 200)
  hitBar = constrain(hitBar, 0, 200)

def drawHitBar():
  text("Click to use " + sword[chosenSword] + " Sword", 120, 250)
  noFill()
  rect(100,200,200,30)
  fill(0, 0, 0)
  rect(100, 200, hitBar, 30)

def mouseClicked():
  swordDamage-= 1

def draw():
  background(116, 126, 176)
  calculateHitBar()
  drawHitBar()
