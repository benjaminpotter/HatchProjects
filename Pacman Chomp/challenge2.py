chompSpeed = 5
pacMouth = 1
pacMouthClose = 0

def draw():
    global pacMouth
    global pacMouthClose
    global chompSpeed
    background(0)
    fill(255, 255, 0)
    pacMouthClose = 360 - pacMouth
    arc(mouseX, mouseY, 80, 80, pacMouth, pacMouthClose)
    if( pacMouth >= 45 or pacMouth <= 0):
       chompSpeed *= -1
    pacMouth += chompSpeed
