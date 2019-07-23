barWidth = 10
hueC = 0

colorMode(HSB, 360)
noStroke()

def draw():
    global hueC
    
    hueC = mouseY
    fill(hueC, 360, 360)
    rect(mouseX, 0, barWidth, height)
    
    fill(0, 0, 0, 10)  
    rect(0, 0, 400, 400) 
