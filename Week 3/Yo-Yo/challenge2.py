def setup():
    size(400, 400)

class Yoyo:

    def __init__(self, y, speed):
        self.x = 11
        self.y = y
        self.speed = speed

    def draw_yoyo(self):
        line(0, self.y, self.x, self.y)
        fill(255, 0, 115)
        ellipse(self.x, self.y, 100, 100)

    def move_yoyo(self):
        self.speed -= 1
        self.x += self.speed

        if self.x < 11:
            self.speed += 2

yoyo1 = Yoyo(100, 20)
yoyo2 = Yoyo(300, 27)

def draw():
    global yoyo1, yoyo2
    
    background(252, 255, 214)
    
    yoyo1.draw_yoyo()
    yoyo1.move_yoyo()
    
    yoyo2.draw_yoyo()
    yoyo2.move_yoyo()
    