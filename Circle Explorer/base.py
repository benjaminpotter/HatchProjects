def setup():
    size(400, 400)
    randomize_circles()

circle_pos = []

def randomize_circles():
    global circle_pos

    for i in range(600):
        circle_pos.append(random(0, 400))

def draw_goal_circle():
    fill(0, 255, 0)
    ellipse(200, 200, 50, 50)

def draw_red_circles():
    global circle_pos

    for i in range(len(circle_pos) / 2):
        fill(255, 0, 0)
        ellipse(circle_pos[i], circle_pos[i + 1], 20, 20)

def check_green_circle():
    if dist(200, 200, mouseX, mouseY) < 50 / 2:
        background(0, 255, 0)
        noLoop()

def check_red_circles():
    global circle_pos

    for i in range(len(circle_pos) / 2):
        if dist(circle_pos[i], circle_pos[i + 1], mouseX, mouseY) < 10:
            background(255, 0, 0)
            noLoop()

def draw():
    draw_red_circles()
    draw_goal_circle()
    check_red_circles()
    check_green_circle()