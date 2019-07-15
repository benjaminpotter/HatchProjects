def setup():
    size(400, 400)

def drawFootball():
    background(50, 130, 13)
    fill(161, 128, 27)
    bezier(50, 200, 100, 75, 300, 75, 350, 200)
    bezier(50, 200, 100, 325, 300, 325, 350, 200)
drawFootball()

def drawStitches():
    noFill()
    stroke(255, 255, 255)
    strokeWeight(10)
    arc(200, 170, 150, 20, 180, 360)
    line(200, 150, 200, 170)
    line(150, 150, 155, 170)
    line(250, 150, 245, 170)
    strokeWeight(10)
    arc(92, 200, 31, 100, 270, 440)
    arc(318, 200, 31, 100, 115, 251)
drawStitches()