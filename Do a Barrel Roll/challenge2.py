spin = 0
lastMouseX = mouseX

def drawBackground():
   background(16, 19, 24)
   fill(150, 150, 0, 110)
   ellipse(50, 50, 10, 10)
   ellipse(125, 97, 10, 10)
   ellipse(200, 305, 10, 10)
   ellipse(75, 260, 10, 10)
   ellipse(260, 190, 10, 10)
   ellipse(270, 350, 10, 10)
   ellipse(350, 20, 10, 10)
   ellipse(360, 260, 10, 10)
   fill(250, 0, 50, 90)
   ellipse(30, 170, 60, 60)
   fill(255, 69, 0, 90)
   ellipse(272, 80, 80, 80)
   fill(211, 211, 211, 90)
   ellipse(350, 380, 50, 50)

def moveShip():
   spin = (mouseX - lastMouseX) * 2
   translate(mouseX, mouseY)
   rotate(spin)
   scale(mouseY / 200)
   translate(-200, -200)

def drawShip():
   noStroke()
   fill(199, 202, 181)
   quad(150, 225, 200, 150, 250, 225, 200, 175)
   triangle(183, 175, 217, 175, 200, 200)
   fill(101, 94, 161)
   quad(170, 185, 175, 160, 180, 185, 175, 220)
   quad(220, 185, 225, 160, 230, 185, 225, 220)
   fill(36, 39, 36)
   rect(194, 160, 12, 20)

def draw():
   drawBackground()
   moveShip()
   drawShip()
   resetMatrix()
