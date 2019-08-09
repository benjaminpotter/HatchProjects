eyeX1 = 120
eyeY1 = 160
eyeX2 = 120
eyeY2 = 290

def drawEyes1():
   fill(255)
   ellipse(120, 160, 100, 100)
   ellipse(280, 160, 100, 100)
   fill(0)
   ellipse(eyeX1, eyeY1, 40, 40)
   ellipse(eyeX1 + 160, eyeY1, 40, 40)

def drawEyes2():
   fill(255)
   ellipse(120, 290, 100, 100)
   ellipse(280, 290, 100, 100)
   fill(0)
   ellipse(eyeX2, eyeY2, 40, 40)
   ellipse(eyeX2 + 160, eyeY2, 40, 40)

def eyeMovement1():
   eyeX1 = map(mouseX, 0, 400, 100, 150)
   eyeY1 = map(mouseY, 0, 400, 140, 190)

def eyeMovement2():
   eyeX2 = map(mouseX, 0, 400, 100, 150)
   eyeY2 = map(mouseY, 0, 400, 270, 320)

def draw():
   background(100, 100, 100)
   drawEyes1()
   drawEyes2()
   eyeMovement1()
   eyeMovement2()
