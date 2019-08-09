rainbowColors = [color(255, 0, 0), color(255, 175, 0), color(255, 255, 0), color(0, 255, 0), color(0, 120, 255), color(170, 0, 255), color(255, 0, 255)]

def drawRainbow():
   noFill()
   strokeWeight(10)
   rainbowSize = 400
   for i in range (0, len(rainbowColors)) :
       stroke(rainbowColors[i] * mouseX)
       arc(200, 400, rainbowSize, rainbowSize, 180, 360)
       rainbowSize -= 20

def drawCloud(x, y) :
   fill(255)
   ellipse(x, y, 75, 50)
   ellipse(x + 50, y, 75, 50)
   ellipse(x + 25, y - 25, 75, 50)

def drawBackground():
   background(0, 200, 255)
   noStroke()
   drawCloud(250, 100)
   drawCloud(0, 150)

def draw():
   drawBackground()
   drawRainbow()
