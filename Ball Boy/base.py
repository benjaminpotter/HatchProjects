def setup():
    size(400, 400)

ball_radius = 10
score = 0
centerX = random(ball_radius, 400 - ball_radius)
centerY = random(ball_radius, 400 - ball_radius)

def draw_tennis_ball(x, y, radius):
    strokeWeight(2)
    fill(0, 255, 38)
    ellipse(x, y, radius * 2, radius * 2)

def pick_up_ball():
    global score, centerX, centerY, ball_radius

    if dist(mouseX, mouseY, centerX, centerY) < ball_radius:
        score += 1
        centerX = random(ball_radius, 400 - ball_radius)
        centerY = random(ball_radius, 400 - ball_radius)

def print_score(score):
    textSize(20)
    fill(255, 255, 255)
    textAlign(CENTER, CENTER)
    text("Balls picked up:\n" + str(score), 200, 350)

def draw():
    global ball_radius, score, centerX, centerY

    background(73, 184, 63)
    draw_tennis_ball(centerX, centerY, ball_radius)
    pick_up_ball()
    print_score(score)
