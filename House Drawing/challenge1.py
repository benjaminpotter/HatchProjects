def drawBackground():
   background(0, 238, 255)
   fill(255, 255, 0)
   ellipse(325, 50, 50, 50)
   fill(0, 255, 0)
   rect(0, 300, 400, 100)

def drawHouse():
   fill(255, 0, 0)
   rect(125, 150, 150, 150)
   fill(0, 0, 255)
   triangle(125, 150, 200, 75, 275, 150)

def drawDoor():
   fill(255, 0, 255)
   rect(175, 200, 50, 100)
   fill(0, 0, 0)
   ellipse(215, 250, 10, 10)

def drawTree():
   fill(165, 42, 42)
   rect(50, 200, 15, 150)
   fill(0, 255, 0)
   ellipse(55, 200, 70, 70)

def draw():
   drawBackground()
   drawHouse()
   drawDoor()
   drawTree()
