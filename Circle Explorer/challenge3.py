def setup():
    size(400, 400)
    textAlign(CENTER, CENTER)
    textSize(20)
    rectMode(CENTER)

difficulty = 1
has_set_difficulty = False
circle_pos = []

lives = 3
cooldown = 0

def randomize_circles():
    global circle_pos, difficulty

    for i in range(100 * difficulty):
        circle_pos.append(random(0, 400))

def draw_goal_circle():
    fill(0, 255, 0)
    ellipse(200, 200, 50, 50)

def draw_red_circles():
    global circle_pos, cooldown 

    for i in range(len(circle_pos) / 2):
        fill(255, 0, 0)
        ellipse(circle_pos[i], circle_pos[i + 1], 20, 20)

def check_green_circle():
    if dist(200, 200, mouseX, mouseY) < 50 / 2:
        background(0, 255, 0)
        noLoop()

def check_red_circles():
    global circle_pos, lives, cooldown
    
    if cooldown < 0:
        for i in range(len(circle_pos) / 2):
            if dist(circle_pos[i], circle_pos[i + 1], mouseX, mouseY) < 10:
                if lives > 1:
                    lives -= 1
                    cooldown = 30
                else:
                    background(255, 0, 0)
                    noLoop()
                    
def draw_lives():
    global lives, cooldown
    
    for i in range(lives):
        strokeWeight(5)
        fill(255, 100, 100)
        rect(40 * i + 25, 25, 30, 30)
            
def keyPressed():
    global circle_pos, difficulty, has_set_difficulty
    
    if has_set_difficulty == False:   
        if keyCode == RIGHT:
            difficulty += 1
        elif keyCode == LEFT:
            difficulty -= 1
            if difficulty < 1:
                difficulty = 1         
        if key == ENTER:
            randomize_circles()
            has_set_difficulty = True

def draw():
    global difficulty, cooldown
    background(255) 
    
    cooldown -= 1
    
    if has_set_difficulty == True:  
        strokeWeight(1)
        draw_red_circles()
        draw_goal_circle()
        draw_lives()
        check_red_circles()
        check_green_circle()
    else:
        fill(0)
        text(difficulty, 200, 200) 