def setup():
    size(400, 400)

class BouncyBall:
    def __init__(self, x_speed, y_speed):
        self.x = random(400)
        self.y = random(400)
        self.x_speed = x_speed
        self.y_speed = y_speed
        
    def moving_ball(self):
        fill(66)
        ellipse(self.x, self.y, 20, 20)
    
        self.x += self.x_speed
        self.y += self.y_speed
    
    def ball_bounce(self):
        if self.x < 0 or self.x > 400:
            self.x_speed *= -1
        
        if self.y < 0 or self.y > 400:
            self.y_speed *= -1

ball1 = BouncyBall(5, 1)
ball2 = BouncyBall(3, 2)
        
def draw():
    global ball1, ball2
    
    background(127, 204, 255)
    ball1.moving_ball()
    ball1.ball_bounce()
    
    ball2.moving_ball()
    ball2.ball_bounce()