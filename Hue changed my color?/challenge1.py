barWidth = 10
hueC = 0
colorMode(HSB)
noStroke()

def draw() :
    hueC = mouseY
    fill(hueC, 355, 355)
    rect(mouseX, 0, barWidth, height)
              
