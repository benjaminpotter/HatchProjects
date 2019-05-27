def setup():
    size(400, 400)

score = 0
timer = 10
last_sec = second()

class Ball:

    def __init__(self):
        self.value = int(random(1, 10))
        self.radius = 10
        self.x = random(self.radius, 400 - self.radius)
        self.y = random(self.radius, 400 - self.radius)
        self.colour = color(random(255), random(255), random(255))

    def draw_self(self):
        strokeWeight(2)
        fill(self.colour)
        ellipse(self.x, self.y, self.radius * 2, self.radius * 2)

ball = Ball()

def pick_up_ball():
    global ball, score

    if dist(mouseX, mouseY, ball.x, ball.y) < ball.radius:
        score += ball.value
        ball = Ball()

def print_score(score):
    textSize(20)
    fill(255, 255, 255)
    textAlign(CENTER, CENTER)
    text("Score:\n" + str(score), 200, 350)
    
def print_timer(timer):
    textSize(20)
    fill(255, 255, 255)
    textAlign(CENTER, CENTER)
    text("Time: " + str(timer), 60, 30)
    
def game_over(score):
    background(73, 184, 63)
    
    textSize(25)
    fill(255, 255, 255)
    textAlign(CENTER, CENTER)
    text("You scored: " + str(score), 200, 200)
    
    noLoop()

def draw():
    global ball, timer, last_sec

    background(73, 184, 63)
    ball.draw_self()
    pick_up_ball()
    print_score(score)
    
    sec = second()
    if sec != last_sec:
        timer -= 1
        last_sec = sec
    print_timer(timer)
    
    if timer == 0:
        game_over(score)