eyeX = 200
eyeY = 320

def drawEyes():
   fill(255)
   ellipse(200, 320, 60, 60)
   ellipse(280, 320, 60, 60)
   fill(0)
   ellipse(eyeX, eyeY, 20, 20)
   ellipse(eyeX + 80, eyeY, 20, 20)

def eyeMovement():
   eyeX = map(mouseX, 0, 400, 180, 220)
   eyeY = map(mouseY, 0, 400, 300, 340)

def draw():
   background(100, 100, 100)
   drawEyes()
   eyeMovement()
