page = "Start"
score = 0
time = millis()
def gameState():
    textAlign(CENTER)
 
    if page == "Start": 
        background(255)
        fill(0)
        textSize(15)
        text("How Many Times Can You Click In 10 Seconds?", 200, 50)
        textSize(50)
        text("Click To Start", 200, 350)
    elif page == "Game":
        fill(255)
        textSize(70)
        text(score, 200, 210)
        textSize(20)
        text(round((millis() - time) / 1000, 1), 100, 100)
    elif page == "End":
        background(255)
        textSize(50)
        fill(0)
        text("Your Score Is:", 200, 180)
        text(floor(score), 200, 240) 

def timer():
    global page
    if (millis() - time) / 1000 > 10:
        page = "End"

def draw():
    background(0)
    gameState()
    timer()
    
def reset():
    global time, score, page
    time = millis()
    score = 0
    page = "Start"

def mouseClicked(e):
    global time, page, score
    if page == "Start":
        page = "Game"
        time = millis()
    elif page == "Game":
        score += 1
    elif page == "End":
        reset()
        time = millis()
    elif page == "Game":
        score += 1
