dPos = [[200, 150], [160, 180], [120, 180], [80, 150],[30, 125], [160, 70]]
oPos = [[200, 220], [200, 250], [200, 270], [200, 290],[160, 220], [120, 220]]
def drawField() :
  background(50, 173, 54)
  strokeWeight(2)
  stroke(255, 255, 255)
  line(0, 200, 400, 200)
  textAlign(CENTER, CENTER)
  textSize(30)
  text("Offense", 200, 375)
  text("Defense", 200, 25)

drawField()
def drawPlayers():
  strokeWeight(10)
  for i in range (0, 2) :
    stroke(0, 0, 255)
    for j in range (0, len(dPos)) :
      point(dPos[j][0], dPos[j][1]) 
    stroke(255, 0, 0)
    for k in range (0, len(oPos)) :
      point(oPos[k][0], oPos[k][1])
    translate(400, 0)
    scale(-1, 1)

drawPlayers()
def drawWideReceivers() :
  point(30, 220)
  point(370, 275)

drawWideReceivers()
def mouseDragged() :
  stroke(255, 255, 0)
  strokeWeight(5)
  point(mouseX, mouseY)  
