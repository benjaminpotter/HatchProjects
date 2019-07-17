class Egg:
    def __init__(self):
        self.x = mouseX
        self.y = mouseY
        self.size = 80
        self.tint = 255
        self.image = getImage("minecraft/egg")
        
    def update(self):
        self.size -= 2
        self.tint -= 10
        self.y += sin(self.size / 20) * 10
        
    def drawEgg(self):
        tint(255, self.tint)
        image(self.image, self.x, self.y, self.size, self.size)

allEggs = [];

def draw():
    imageMode(CENTER);
    background(0, 0, 0);
    for egg in allEggs:
        egg.drawEgg();
        if egg.size > 1:
            egg.update();
        else:
            allEggs.remove(egg);

def mouseClicked():
    allEggs.append(Egg());