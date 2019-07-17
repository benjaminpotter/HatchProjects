def drawLogoBase():
    stroke(0, 0, 0)
    strokeWeight(2)
    fill(255, 0, 0)
    triangle(75, 150, 325, 150, 200, 300)
    quad(75, 150, 110, 100, 290, 100, 325, 150)
    stroke(255, 0, 0)
    strokeWeight(4)
    line(80, 150, 320, 150)
drawLogoBase()

def drawS():
    stroke(0, 0, 0)
    strokeWeight(2)
    fill(255, 242, 0)
    quad(100, 150, 120, 120, 150, 120, 115, 170)
    triangle(235, 120, 260, 120, 260, 135)
    triangle(280, 120, 280, 175, 300, 150)
    triangle(280, 175, 280, 140, 170, 138)
    arc(200, 140, 80, 40, 50, 360)
    triangle(200, 275, 170, 240, 230, 240)
    arc(200, 210, 80, 20, 270, 450)
    quad(200, 220, 200, 200, 130, 180, 160, 210)
    fill(255, 0, 0)
    arc(146, 155, 66, 65, 150, 275)
    stroke(255, 242, 0)
    strokeWeight(4)
    line(200, 203, 200, 215)
    line(280, 170, 280, 143)
drawS()