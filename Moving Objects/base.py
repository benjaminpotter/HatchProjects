numBalls = 11
balls = []

def createBall():
    balls.append({'x': random(50, 350), 'y': random(50, 350)})

for i in range(numBalls):
    createBall()

def updateBalls(balls):
    for b in balls:
        b['y'] += 1
        if b['y'] > 410:
            b['y'] = -10

def drawBalls(balls):
    fill(0, 100, 150)
    for b in balls:
        ellipse(b['x'], b['y'], 12, 12)

def draw():
    background(255, 255, 255)
    updateBalls(balls)
    drawBalls(balls)