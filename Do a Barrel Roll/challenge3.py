spin = 0
lastMouseX = mouseX

def drawBackground():
   background(16, 19, 24)

def moveShip():
   spin = (mouseX - lastMouseX) * 2
   translate(mouseX, mouseY)
   rotate(spin)
   scale(mouseY / 200)
   translate(-200, -200)

def drawShip1():
   noStroke()
   fill(199, 202, 181)
   quad(150, 225, 200, 150, 250, 225, 200, 175)
   triangle(183, 175, 217, 175, 200, 200)
   fill(101, 94, 161)
   quad(170, 185, 175, 160, 180, 185, 175, 220)
   quad(220, 185, 225, 160, 230, 185, 225, 220)
   fill(36, 39, 36)
   rect(194, 160, 12, 20)

def drawShip2():
   noStroke()
   fill(199, 202, 181)
   ellipse(200, 175, 20, 20)
   rect(150, 175, 100, 10)
   triangle(183, 175, 217, 175, 200, 200)
   fill(90, 150, 60)
   quad(170, 185, 175, 160, 180, 185, 175, 220)
   quad(220, 185, 225, 160, 230, 185, 225, 220)

def draw():
   drawBackground()
   moveShip()
   drawShip1()
   translate(-100, 0)
   drawShip2()
   resetMatrix()
