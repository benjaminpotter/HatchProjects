txt = "Hello World!"
trailColor = color(102, 74, 64)
mainColor = color(146, 179, 121)
depthMax = 40
depthMin = 15
depthAmount = 8 / len(txt)
angle = 24
angleMode = "radians"
x = 0
y = height / 2
w = cos(angle)
h = sin(angle)
depths = []
dirs = []
txtWidth = 0
textSize(58)

def createText():
    for j in range(len(txt)):
        depths[j] = cos(PI / 2 * j / txt.length) * (depthMax - depthMin) + depthMin
        dirs[j] = 1
        txtWidth += textWidth(txt[j])
createText()

def drawText():
    w = cos(angle)
    h = sin(angle)

    if angle >= PI / 2 and angle < PI * 3 / 2:
        offsetX = 0
        for j in range(len(txt)):
            x = width / 2 - txtWidth / 2
            for i in range(depths[j]):
                if i < depths[j] - 1:
                    fill(trailColor)
                else:
                    fill(mainColor)
                text(txt.charAt(j), x + offsetX + i * w, y + i * h)
        offsetX += textWidth(txt.charAt(j))
    else:
        offsetX = 0
        for j in range(len(txt) - 1, 0, -1):
            offsetX += textWidth(txt.charAt(j))
            x = width / 2 + txtWidth / 2
            for i in range(depths[j]):
                if i < depths[j] - 1:
                    fill(trailColor)
                else:
                    fill(mainColor)
        text(txt.charAt(j), x - offsetX + i * w, y + i * h)


def updateDepth():
    for j in range(len(txt)):
        depths[j] += depthAmount * dirs[j]
        if depths[j] > depthMax:
            depths[j] = depthMax
            dirs[j] *= -1
        elif depths[j] < depthMin:
            depths[j] = depthMin
            dirs[j] *= -1

def draw():
    background(0, 0, 0)
    drawText()
    updateText()