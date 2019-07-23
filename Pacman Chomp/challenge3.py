chompSpeed = 5
pacMouth = 1
pacMouthClose = 0
pacPosX = -40


def draw():
    global pacMouth
    global pacMouthClose
    global chompSpeed
    global pacPosX 
    background(0)
    fill(255, 255, 0)
    pacMouthClose = 360 - pacMouth
    arc(pacPosX, 200, 80, 80, pacMouth, pacMouthClose) 
    if(pacMouth >= 45 or pacMouth <= 0): 
        chompSpeed *= -1 
    pacMouth += chompSpeed
    pacPosX += 3
    if (pacPosX > 440):  
        pacPosX = -40
    if (pacPosX < 200): 
        fill(255)
        ellipse(200, 200, 15, 15)  
    
