flowerList = []
numOfPetals = 10
chance = 40

class Flower:

    def __init__(self):
        self.xPos = random(0, 390)
        self.yPos = -20
        self.speed = random(1, 3)
        self.rotation = random(1, 5)

def drawFlower():
    for r in range(numOfPetals):
        fill(173, 186, 173)
        rotate(360 / numOfPetals)
        ellipse(0, 0, 60, 10)
    noStroke()
    fill(224, 255, 150)
    ellipse(0, 0, 20, 20)

def moveFlowers():
    for flower in flowerList:
        flower.yPos += flower.speed
        flower.rotation -= random(1, 3)
        translate(flower.xPos, flower.yPos)
        rotate(flower.rotation)
        drawFlower()
        resetMatrix()

def startFlower():
    trial = random(0, chance)
    roundedTrial = round(trial)
    if roundedTrial == 1:
        flowerList.append(Flower())

def draw():
    background(245, 224, 173)
    startFlower()
    moveFlowers()