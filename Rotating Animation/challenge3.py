angle = 0

def moveSquare():
   global angle
   translate(200,200)
   rotate(angle)
   fill(mouseX, 100, mouseY)
   rect(45, 45, 100, 100)
   angle += 2
   resetMatrix()

def draw():
   moveSquare()
