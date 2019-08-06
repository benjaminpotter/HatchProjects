topPos = 190
bottomPos = 220

def drawLines(y) :
   line(100, y, 166, y - 30)
   line(166, y - 30, 232, y)
   line(232, y, 297, y - 30)

def drawEgg():
   background(0, 118, 165)
   stroke(255)
   strokeWeight(10)
   noFill()
   arc(200, topPos, 200, 280, 180, 345)
   drawLines(topPos)
   drawLines(bottomPos)
   arc(200, bottomPos, 200, 250, 346, 540)
   fill(255, 255, 255)
   textAlign(CENTER)
   textSize(20)
   text("Change the World", 200, 380)
drawEgg()
