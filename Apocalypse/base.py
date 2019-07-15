class Enemy:
    def __init__(self):
        self.x = 375
        self.y = random(25, 375)
        self.size = 15
        self.speed = -10
        
enemy = Enemy()

def drawHero():
    fill(0, 255, 55)
    ellipse(mouseX, mouseY, 50, 50)

def drawBackground():
    background(154, 161, 252)

def drawEnemy():
    fill(255, 0, 0)
    ellipse(enemy.x, enemy.y, enemy.size, enemy.size)
    enemy.x += enemy.speed

def resetEnemy():
    if enemy.x < -15:
        enemy.x = 385
        enemy.y = random(25, 375)
        enemy.size += 1
        enemy.speed -= 0.3

def checkCollision():
    if dist(enemy.x, enemy.y, mouseX, mouseY) < enemy.size:
        background(0, 0, 0)

def draw():
    drawBackground()
    drawHero()
    drawEnemy()
    resetEnemy()
    checkCollision()