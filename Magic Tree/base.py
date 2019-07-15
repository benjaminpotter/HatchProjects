numOfDots = 200
angleChange = 137
maxRadius = 400
noStroke()
fill(252, 219, 86)

def draw():
    background(26, 26, 26)
    for i in range(numOfDots):
        radius = maxRadius * (i / numOfDots)
        theta = angleChange * i
        x = 200 + radius * cos(theta)
        y = 10 + radius
        ellipse(x, y, 5, 5)
    angleChange += 0.001
