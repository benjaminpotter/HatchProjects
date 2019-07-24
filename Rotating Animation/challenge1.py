angle = 0

def moveSquare():
   global angle
   translate(200, 200)
   rotate(angle)
   fill(mouseX, 100, mouseY)
   rect(25, 25, 100, 100)
   angle += 5
   resetMatrix()

def draw():
   moveSquare()
