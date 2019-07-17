manyObstacles = []
gameOver = False
holeSize = 75
counter = 0
charY = 100

class Obstacle:

    obstacleHeight = 30
    obstacleSpeed = 2

    def __init__(self, y):
        self.width = random(75, 325)
        self.start2 = self.width + holeSize
        self.y = y

manyObstacles.append(Obstacle(400))
manyObstacles.append(Obstacle(575))
manyObstacles.append(Obstacle(725))

def deleteObstacles():
    if manyObstacles[0].y < -Obstacle.obstacleHeight:
        manyObstacles.pop(0)
        manyObstacles.append(Obstacle(450))
    if random(0, 8) < 1:
        Obstacle.obstacleSpeed += 1

def drawObstacles():
    for i in range(len(manyObstacles)):
        fill(0)
        rect(0, manyObstacles[i].y, manyObstacles[
             i].width, Obstacle.obstacleHeight)
        rect(manyObstacles[i].start2, manyObstacles[
             i].y, 400, Obstacle.obstacleHeight)

def moveObstacles():
    for i in range(len(manyObstacles)):
        manyObstacles[i].y -= Obstacle.obstacleSpeed

def moveCharacter():
    global charY

    fill(255, 0, 0)
    ellipse(mouseX, charY, 60, 60)
    if get(mouseX, charY + 30) == color(0, 0, 0):
        charY -= Obstacle.obstacleSpeed
    elif charY < 350:
        charY += Obstacle.obstacleSpeed

def ceilingCollision():
    if charY < 0:
        gameOver = True

def draw():
    if gameOver == False:
        background(255)
        drawObstacles()
        moveObstacles()
        deleteObstacles()
        moveCharacter()
        ceilingCollision()
    else:
        background(255, 0, 0)
