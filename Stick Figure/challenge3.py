stroke(0, 0, 0)
strokeWeight(4)
def drawOutLine():
    fill(255, 224, 189)
    ellipse(195, 90, 105, 105)
    line(195, 143, 192, 277)
    line(136, 372, 191, 276)
    line(195, 277, 248, 370)
    line(193, 147, 135, 236)
    line(195, 145, 255, 238)
drawOutLine()
def drawFace():
   point(175, 75)  
   point(215, 75)
   noFill()
   arc(195, 105, 40, 20, 20, 160)
drawFace()

