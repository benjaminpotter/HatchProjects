heroX = 50
heroY = 200
heroImg = getImage("space/octopus")
projectileSpeed = 3
projectiles = []
imageMode(CENTER)

class Projectile:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def moveHero():
    image(heroImg, heroX, heroY, 80, 80)
    heroY = constrain(mouseY, 30, 350)

def moveProjectile():
    for p in projectiles:
        p.x += projectileSpeed
        ellipse(p.x, p.y, 10, 10)

def mouseClicked():
    projectiles.append(Projectile(heroX, heroY))

def draw():
    background(0)
    moveHero()
    moveProjectile()
