noStroke()

def mouseClicked():
    fill(random(0, 255), random(0, 255), random(0, 255));

def draw():
   mouseDist = dist(200, 200, mouseX, mouseY)
   for i in range(0,18):
       resetMatrix()
       translate(200, 200)
       rotate(i * 20)
       ellipse(0, mouseDist, mouseDist / 2, mouseDist / 2)

