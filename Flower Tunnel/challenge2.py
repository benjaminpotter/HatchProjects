stroke(0)
def mouseClicked(e):
   fill(random(0, 255), random(0, 255), random(0, 255))

def draw(): 
   mouseDist = dist(200, 200, mouseX, mouseY)
   for i in range(1,19):
       resetMatrix()
       translate(200, 200)
       rotate(i * 20)
       rect(0, mouseDist, mouseDist / 2, mouseDist / 2)
