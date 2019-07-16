a = color(165, 167, 20)
b = color(77, 86, 59)
c = color(42, 106, 105)
d = color(165, 89, 20)
e = color(146, 150, 127)
barWidth = 5

def drawBand(v, w, x, y, z, start):
    num = 5
    colors = [v, w, x, y, z]

    for i in range(0, 400, barWidth * num):
        for j in range(0, num):
            fill(colors[j])
            rect(i + j * barWidth, start, barWidth, 400 / 2)

def draw():
    noStroke()
    drawBand(a, b, c, d, e, 0)
    drawBand(c, a, d, b, e, 400 / 2)