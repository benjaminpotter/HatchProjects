def setup():
    size(400, 400)
    
x_speed = 3
y_speed = 4
x_pos = 0
y_pos = 200

class Ball:
    def __init__(self, x, y, xspeed, yspeed):
        self.x = x
        self.y = y
        self.x_speed = xspeed
        self.y_speed = yspeed
        
    def draw_ball(self):
        stroke(255, 0, 0)
        strokeWeight(15)
        point(self.x, self.y)
        self.x += self.x_speed
        self.y += self.y_speed
        
    def loop_ball(self):
        if self.x > 412:
            self.x = -12
        elif self.y > 412:
            self.y = - 12

ball1 = Ball(0, 200, 3, 4)
ball2 = Ball(0, 200, 4, 3)
        
def draw():
    global ball1, ball2
    
    background(100)
    ball1.draw_ball()
    ball1.loop_ball()
    
    ball2.draw_ball()
    ball2.loop_ball()
