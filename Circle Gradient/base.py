def setup():
    size(400, 400)

radius = width
circleHue = 0

def drawGradient():
    circleHue + +
    for r in range(radius, 0, -1):
        fill(circleHue, 90, 90)
        ellipse(200, 200, r, r)
        circleHue = (circleHue + 1) % 360

def draw():
    colorMode(HSB, 360, 100, 100)
    noStroke()
    frameRate(15)
    background(0)
    drawGradient()
    fill(255)