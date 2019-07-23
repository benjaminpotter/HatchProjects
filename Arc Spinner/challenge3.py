angles = [0, 0, 0, 0]
numClicks = 0
level = 1
def drawArcs() :
   start = [0, 0, 0, 0]
   end = [0, 0, 0, 0]
   noFill()
   stroke(0, 255, 255)
   strokeCap(SQUARE)
   strokeWeight(20)
   for i in range (0, 4) :
       start[i] = 110 + angles[i]
       end[i] = 430 + angles[i]
       arcPos = 100 + (4-i) * 50    
       arc(200, 200 , arcPos, arcPos, start[i], end[i])

def spinArcs():
    global numClicks
    for i in range (0, 4) :
       if numClicks < i + 1 :
           angles[i] += i + level
           
def checkWin():
    global numClicks
    if abs(angles[1] % 360 - angles[2] % 360) < 30 and abs(angles[2] % 360 - angles[2] % 360) < 30 and abs(angles[3] % 360 - angles[3] % 360) < 30 :
           text("Path Open, You WIN", 200, 200)
           text("Click to play next level", 200, 225)
           if mousePressed :
               numClicks = 0
               level+=1
    else :
        text("Game Over, You Lose", 200, 200)

            
def mouseClicked() :
    global numClicks
    numClicks += 1
    
def draw() :
    background(0, 0, 0)
    spinArcs()
    checkWin()
    drawArcs()
