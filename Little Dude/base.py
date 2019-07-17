healthStat = 10
loveStat = 10
happyStat = 10
dudeText = ""
def drawButtons():
  noFill()
  rect(20,320,100,40)
  rect(150,320,100,40)
  rect(280,320,100,40)
  textSize(11)
  text("Feed The Dude",34,345)
  text("Hug The Dude",167,345)
  text("Play with the Dude",285,345)

def setup():
    size(400,400)


def drawStats(): 
  fill(117, 61, 61)
  textSize(20)
  text("Health: " + str(healthStat), 20, 40)
  text("Love: " + str(loveStat), 140,40)
  text("Happiness: " + str(happyStat), 250,40)

def drawDude():
  stroke(0, 0, 0)
  noFill()
  ellipse(200,200,100,100)
  ellipse(180,180,10,10)
  ellipse(220,180,10,10)

def drawSmile():
  if (happyStat < 5 or loveStat < 5 or healthStat < 5): 
    arc(200,235,60,50,205,330)
  elif (happyStat < 7 or loveStat < 7 or healthStat < 7):
    line(175,220,225,220)
  elif(): 
    arc(200,200,60,50,30,150)
  

def displayCaption():
  textSize(20)
  text(dudeText, 150,100)

def checkGameOver():
  if (happyStat < 3 or loveStat < 3 or healthStat < 3): 
    background(20, 0, 0)
    fill(255, 0, 0)
    textSize(30)
    text("You killed the Little Dude!",25,140)
  

def draw():
  background(255, 255, 255)
  drawButtons()
  drawStats()
  drawDude()
  drawSmile()
  displayCaption()
  checkGameOver()

def mouseClicked():
  if (mouseX > 20 and mouseX < 120 and mouseY > 320 and mouseY < 360): 
    healthStat += round(random(2,4))
    loveStat -= round(random(1,2))
    happyStat -= round(random(1,2))
    dudeText = "Food! Yay!"
  
  if (mouseX > 150 and mouseX < 250 and mouseY > 320 and mouseY < 360): 
      global loveStat
      global healthStat
      global happyStat
      global dudeText
  loveStat += round(random(2,4))
  healthStat -= round(random(1,2))
  happyStat -= round(random(1,2))
  dudeText = "Aww... Thanks!"
  
  if (mouseX > 280 and mouseX < 380 and mouseY > 320 and mouseY < 360):
    happyStat += round(random(2,4))
    loveStat -= round(random(1,2))
    healthStat -= round(random(1,2))
    dudeText = "I love games!"
  
