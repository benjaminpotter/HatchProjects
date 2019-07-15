def setup():
    size(400, 400)
    background(255)
    x = 150
    y = 200
    scale(1.4)
    noStroke()
    fill(0, 0, 0)
    rect(x - 150, y - 100, 300, 100)
    fill(255, 255, 255)
    rect(x - 60, y - 140, 120, 60, 50)
    arc(x - 150, y - 50, 120, 100, 270, 450)
    arc(x + 150, y - 50, 120, 100, 90, 270)
    ellipse(x - 100, y, 200, 90)
    ellipse(x + 100, y, 200, 90)
    fill(0, 0, 0)
    rect(x - 7.5, y - 90, 15, 30)
    triangle(x - 17.5, y - 60, x - 2.5, y - 60, x - 7.5, y - 97)
    triangle(x + 17.5, y - 60, x + 2.5, y - 60, x + 7.5, y - 97)
