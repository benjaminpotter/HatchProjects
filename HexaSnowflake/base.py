numOfSpokes = 6
def drawSetup() :
  background(255, 255, 255)
  translate(200, 200)
  scale(1.4, 1.4)
  stroke(89, 184, 235)

drawSetup()
def drawSpoke() :
 strokeWeight(10)
 line(0, 5, 0, 120)
 strokeWeight(8)
 line(0, 23, 17, 32)
 line(0, 23, -17, 32)
 line(0, 48, 21, 76)
 line(0, 48, -21, 76)
 strokeWeight(6)
 line(0, 80, 12, 106)
 line(0, 80, -12, 106)

for spokes in range (0, numOfSpokes) :
 drawSpoke()
 rotate(360 / numOfSpokes)
