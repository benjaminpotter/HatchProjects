angle = 0

def moveSquare():
   global angle
   translate(mouseX, mouseY)
   rotate(angle)
   fill(mouseX, 100, mouseY)
   rect(25, 25, 100, 100)
   angle += 2
   resetMatrix()

def draw():
   moveSquare()
