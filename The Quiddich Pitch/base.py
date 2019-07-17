def drawHoops(x1, x2, x3):
    noFill()
    stroke(0, 0, 0)
    strokeWeight(3)
    ellipse(x1, 160, 20, 40)
    line(x1, 180, x1, 340)
    ellipse(x2, 100, 20, 40)
    line(x2, 120, x2, 330)
    ellipse(x3, 150, 20, 40)
    line(x3, 170, x3, 320)

def drawBackground():
    noStroke()
    background(156, 176, 206)
    fill(90, 147, 66)
    rect(0, 300, 400, 200)
    drawHoops(20, 40, 60)
    drawHoops(360, 340, 320)
drawBackground()

def drawBalls():
    strokeWeight(1)
    fill(178, 26, 26)
    ellipse(random(100, 300), random(10, 300), 15, 15)
    fill(66, 66, 66)
    ellipse(random(100, 300), random(10, 300), 10, 10)
    ellipse(random(100, 300), random(10, 300), 10, 10)
    fill(234, 218, 42)
    snitchX = random(0, 400)
    snitchY = random(0, 400)
    triangle(snitchX, snitchY, snitchX - 6, snitchY - 7, snitchX - 6, snitchY - 2)
    triangle(snitchX, snitchY, snitchX + 6, snitchY - 7, snitchX + 6, snitchY - 2)
    ellipse(snitchX, snitchY, 5, 5)
drawBalls()

def setColor(house):
    if house == "Gryffindor":
        fill(178, 26, 26)
    if house == "Ravenclaw":
        fill(49, 68, 145)
    if house == "Hufflepuff":
        fill(224, 181, 24)
    if house == "Slytherin":
        fill(49, 124, 67)

def drawPlayer(x, y, house):
    offset = random(0, 200)
    fill(252 - offset, 226 - offset, 184 - offset)
    ellipse(x, y - 15, 10, 10)
    fill(84, 58, 6)
    ellipse(x, y + 10, 30, 5)
    setColor(house)
    ellipse(x, y, 10, 20)

def drawTeam(house):
    for i in range(1, 8):
        drawPlayer(random(10, 390), random(20, 290), house)
drawTeam("Ravenclaw")
drawTeam("Hufflepuff")
