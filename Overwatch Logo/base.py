startGrey = -40
endGrey = 220
startOrange = 225
endOrange = 315
def drawArcs():
    noFill()
    strokeCap(SQUARE)
    strokeWeight(30)
    stroke(100)
    arc(200, 200, 200, 200, startGrey, endGrey)
    stroke(255, 160, 0)
    arc(200, 200, 200, 200, startOrange, endOrange)
    
drawArcs()

def drawElements():
    stroke(100)
    line(130, 270, 185, 220)
    line(215, 220, 270, 270)
    noStroke()
    fill(100)
    triangle(170, 220, 195, 232, 195, 145)
    triangle(230, 220, 205, 230, 205, 145)

drawElements()
