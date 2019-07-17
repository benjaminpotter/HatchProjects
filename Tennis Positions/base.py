counter = 0
i = 0
positions = [[200, 250], [80, 370], [320, 370]]
texts = ["Ready Position", "Forehand", "Backhand"]
img = getImage("avatars/old-spice-man")

def drawTennisRacket():
  if counter < 100 :
    fill(0, 0, 0)
    textSize(50)
    textAlign(CENTER,CENTER)
    text(texts[i], 200, 100)
    stroke(0, 13, 255)
    strokeWeight(10)
    line(200, 370, positions[i][0], positions[i][1])

def updateRacket():
  if counter >= 100 :
    if i == 1 || i == 2
      i = 0
    elif round(random(0, 1)) == 0 :
      i = 1
    else :
      i = 2
  counter = 0

def draw() :
  background(133, 217, 217)
  image(img, 140, 273)
  counter++
  drawTennisRacket()
  updateRacket()
