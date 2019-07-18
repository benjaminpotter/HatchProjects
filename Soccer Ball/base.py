def setup():
    size(400, 400)

def drawBall():
    noStroke()
    fill(150, 142, 142)
    ellipse(200, 290, 200, 30)
    fill(0, 0, 0)
    ellipse(200, 200, 200, 200)
drawBall()

def drawPatches():
    fill(255, 255, 255)
    translate(200, 200)
    for i in range(1, 6):
        rotate(72)
        quad(-25, -35, -25, -95, 25, -95, 25, -35)
        triangle(-24, -35, -24, -95, -46, -65)
        triangle(24, -35, 24, -95, 46, -65)
drawPatches()
