InsideOutside = 1
def draw():
    if InsideOutside == 1: 
       background(255, 255, 255)
       fill(255, 255, 255)
       ellipse(50, 50, 50, 50)
       rect(0, 300, 400, 100)
       rect(100, 150, 200, 200)
       rect(175, 250, 50, 100)
def setup():
    size(400,400) 
def mouseClicked():
    if (mouseX > 175 and mouseX < 225 and mouseY > 250 and mouseY < 350):
        InsideOutside = 0
    else: 
       background(160, 82, 42)
       fill(160, 82, 42)
       xmasTree = getImage("seasonal/xmas-tree-with-presents")
       image(xmasTree, 100, 50, 275, 325)
       rect(30, 265, 50, 100)
       ellipse(40, 315, 10, 10)
def mouseClicked():
    if (mouseX > 30 and mouseX < 80 and mouseY > 265 and mouseY < 365): 
        InsideOutside = 1
        mouseClicked()
