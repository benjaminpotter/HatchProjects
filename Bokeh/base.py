manyLights = []
lightSize = 55

class Light:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animated = False
        self.brightness = 0
        self.fadeAmount = 4
        self.color = color(255, random(100, 255), random(150, 255))

def createLights():
    for x in range(400):
        for y in range(400):
            manyLights.append(Light(x, y))
createLights()

def drawLights():
    for i in range(len(manyLights)):
        fill(manyLights[i].color, manyLights[i].brightness)
    ellipse(manyLights[i].x, manyLights[i].y, lightSize, lightSize)

def updateLights():
    manyLights[int(random(0, len(manyLights) - 1))].animated = True
    for i in range(len(manyLights)):
        if manyLights[i].animated:
            manyLights[i].brightness += manyLights[i].fadeAmount
        if manyLights[i].brightness > 255:
            manyLights[i].fadeAmount = -manyLights[i].fadeAmount
        if manyLights[i].brightness < 0:
            manyLights[i].fadeAmount = -manyLights[i].fadeAmount
            manyLights[i].animated = false

def draw():
    background(0)
    drawLights()
    updateLights()