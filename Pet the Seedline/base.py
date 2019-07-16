phrases = ["That tickles!”, "ouch!", "Hey, Leave me alone!"]
phraseNumber = 0
def drawScene() :
  background(255, 255, 255)
  fill(181, 181, 181)
  textSize(40)
  text("Pet the Seedling!", 61, 53)
  image(getImage("avatars/leafers-seed"), 140,120, 150, 150)

def displayPhrase():
  if mouseIsPressed :
    if mouseX > 140 and mouseX < 290 and mouseY > 120 and mouseY < 270 :
      fill(130, 191, 90)
      textSize(20)
      text(phrases[phraseNumber], 241, 147)

def mouseClicked() :
  phraseNumber = round(random(0,phrases.length-1))

def draw():  
  drawScene()
  displayPhrase()
