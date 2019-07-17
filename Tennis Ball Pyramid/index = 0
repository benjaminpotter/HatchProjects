index = 0
class Character:

    def __init__(self):
        self.name = ["Hopper", " Squid", "Winston", "Piceratops", "Leafers"]
        self.image = [getImage("creatures/hopper-happy"), getImage("avatars/orange-juice-squid"), getImage(
            "creatures/winston"), getImage("avatars/piceratops-sapling"), getImage("avatars/leafers-sapling")]
        self.power = [5, 2, 6, 8, 8]
        self.toughness = [5, 3, 6, 3, 4]
        self.speed = [5, 10, 3, 4, 3]

character = Character()

def drawText():
    textSize(25)
    fill(128, 128, 128)
    text("CHARACTER SELECTOR", 52, 51)
    textSize(35)
    fill(255, 234, 0)
    text(character.name[index], 140, 109)
    textSize(20)
    text("Power: " + character.power[index], 150, 325)
    text("Toughness: " + character.toughness[index], 130, 350)
    text("Speed: " + character.speed[index], 150, 375)

def drawCharacter():
    fill(212, 212, 212)
    noStroke()
    ellipse(198, 270, 86, 40)
    image(character.image[index], 130, 140, 140, 140)

def drawArrows():
    image(getImage("cute/RampWest"), 30, 195, 45, 50)
    image(getImage("cute/RampEast"), 325, 195, 45, 50)

def draw():
    background(255, 255, 255)
    drawText()
    drawCharacter()
    drawArrows()

def changeCharacter():
    if mouseY > 195 and mouseY < 245:
        if mouseX > 325 and mouseX < 365:
            index += 1
    elif mouseX > 30 and mouseX < 75:
        index -= 1

def loopCharacter():
    if index < 0:
        index = len(character.name) - 1
    elif index > len(character.name) - 1:
        index = 0

def mouseClicked():
    changeCharacter()
    loopCharacter()
