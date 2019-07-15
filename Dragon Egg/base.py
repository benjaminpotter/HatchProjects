def drawFireplace():
    noStroke()
    background(79, 17, 0)
    fill(191, 105, 63)
    rect(75, 75, 250, 250)

def drawEgg():
    translate(200, 240)
    rock = random(-15, 15)
    rotate(rock)
    fill(50, 50, 50)
    ellipse(0, 0, 100, 150)
    resetMatrix()

def drawFire():
    fill(224, 127, 0)
    triangle(80, 325, 100, 230, 220, 325)
    fill(160, 32, 32)
    triangle(100, 325, 140, 250, 200, 325)
    fill(219, 110, 37)
    triangle(130, 325, 210, 230, 250, 325)
    fill(160, 32, 32)
    triangle(270, 325, 250, 250, 220, 325)
    fill(224, 127, 0)
    triangle(230, 325, 280, 260, 320, 325)

def draw():
    drawFireplace()
    drawEgg()
    drawFire()