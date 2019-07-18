class Brick:
    def __init__(self):
        self.xPos = 24
        self.yPos = 42
        self.On = True
         
class Ball:
    def __init__(self):
        self.xPos = 200
        self.yPos = 200
        self.xSpeed = random(-5, 5)
        self.ySpeed = 5
        
brick = Brick()
ball = Ball() 

brickW = 341
brickH = 112
rand = 0
index = 0 
def drawBricks():
    fill(250, 87, 87)
    if brick.On == True:
        rect(brick.xPos, brick.yPos, brickW, brickH)
 
def drawBall():
    fill(66, 66, 66)  
    ellipse(ball.xPos, ball.yPos, 6, 6)
    ball.xPos = ball.xPos + ball.xSpeed
    ball.yPos = ball.yPos + ball.ySpeed

def bounceBall():
    if ball.xPos < 0 or ball.xPos > 400:
        ball.xSpeed = -ball.xSpeed
    if ball.yPos < 0 or  ball.yPos > 400:
        ball.ySpeed = -ball.ySpeed
 
def breakBrick():
    print(brick)
    if brick.On == True:
        if brick.yPos < ball.yPos and ball.yPos < brick.yPos + brickH and brick.xPos < ball.xPos and ball.xPos < brick.xPos+brickW:
            brick.On = False
            closestYDistance = min(abs(ball.yPos - brick.yPos), abs(ball.yPos - (brick.yPos + brickH)))
            closestXDistance = min(abs(ball.xPos - brick.xPos), abs(ball.xPos - (brick.xPos + brickW)))
            if closestYDistance < closestXDistance:
                ball.ySpeed = -ball.ySpeed
            else:
                ball.xSpeed = -ball.xSpeed
                
def draw():
    background(127, 255, 238)
    drawBricks()
    drawBall()
    bounceBall()
    breakBrick()
