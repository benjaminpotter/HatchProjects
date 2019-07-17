def drawBalloons():
    background(201, 250, 255)
    for j in range(50):
        stroke(255)
        line(200, 250, random(125, 275), 150)
    noStroke()
    for i in range(200):
        fill(random(0, 255), random(0, 255), random(0, 255), 200)
        ellipse(random(70, 340), random(0, 150), 20, 30)
        ellipse(random(125, 275), random(0, 200), 20, 30)
drawBalloons()

def drawHouse():
    stroke(255)
    strokeWeight(3)
    fill(154, 205, 225)
    rect(100, 300, 200, 150)
    fill(250, 156, 137)
    rect(100, 325, 125, 75)
    fill(199, 210, 137)
    rect(225, 325, 75, 75)
    fill(99, 71, 56)
    quad(100, 300, 275, 300, 270, 250, 120, 250)
    fill(253, 246, 207)
    rect(225, 300, 75, 25)
    triangle(225, 300, 300, 300, 265, 200)
drawHouse()

def drawDetails():
    fill(99, 71, 56)
    rect(190, 350, 25, 100)
    line(100, 390, 223, 390)
    line(180, 395, 220, 395)
    fill(100)
    rect(130, 340, 20, 30)
    rect(235, 340, 20, 30)
    rect(270, 340, 20, 30)
    rect(252, 260, 20, 30)
drawDetails()
