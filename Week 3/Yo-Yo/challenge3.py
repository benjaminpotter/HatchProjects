def setup():
    size(400, 400)

class Yoyo:

    def __init__(self, x, speed):
        self.x = x
        self.y = 11
        self.speed = speed

    def draw_yoyo(self):
        line(self.x, 0, self.x, self.y)
        fill(255, 0, 115)
        ellipse(self.x, self.y, 100, 100)
        
        #face
        fill(0)
        ellipse(self.x + 30, self.y, 10, 10)
        ellipse(self.x - 30, self.y, 10, 10)
        if self.speed > 0:
            arc(self.x, self.y + 20, 30, 20, PI, PI * 2)
        else:
            arc(self.x, self.y + 20, 30, 20, 0, PI)

    def move_yoyo(self):
        self.speed -= 1
        self.y += self.speed

        if self.y < 11:
            self.speed += 2

yoyo1 = Yoyo(200, 27)

def draw():
    global yoyo1
    
    background(252, 255, 214)
    
    yoyo1.draw_yoyo()
    yoyo1.move_yoyo()