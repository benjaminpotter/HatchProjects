def setupField():
    background(60, 153, 55)
    stroke(255, 255, 255)
    strokeWeight(1)
    noFill()
    rectMode(CENTER)
    rect(200, 200, 350, 200)
setupField()

def drawYardLines():
    textAlign(CENTER, CENTER) 
    textSize(12)
    for i in range(20):
        strokeWeight(1)
        x = map(i, 0, 20, 60, 340)
        line(x, 100, x, 300) 
        if i % 2 == 0 and i > 1 and i < 19:
            label = 50 - 10 * abs(10 - i) / 2
            text(label, x, 110)
            text(label, x, 290)  
drawYardLines()

def drawGoalPosts():
    strokeWeight(5)
    stroke(247, 255, 0)
    for i in range(2):
        line(16, 200, 23, 200)
        line(15, 181, 15, 219) 
        line(14, 180, 5, 180)
        line(14, 220, 5, 220)
        translate(400, 0)
        scale(-1, 1)
drawGoalPosts()def setupField():
    background(60, 153, 55)
    stroke(255, 255, 255)
    strokeWeight(1)
    noFill()
    rectMode(CENTER)
    rect(200, 200, 350, 200)
setupField()

def drawYardLines():
    textAlign(CENTER, CENTER) 
    textSize(12)
    for i in range(20):
        strokeWeight(1)
        x = map(i, 0, 20, 60, 340)
        line(x, 100, x, 300) 
        if i % 2 == 0 and i > 1 and i < 19:
            label = 50 - 10 * abs(10 - i) / 2
            text(label, x, 110)
            text(label, x, 290)  
drawYardLines()

def drawGoalPosts():
    strokeWeight(5)
    stroke(247, 255, 0)
    for i in range(2):
        line(16, 200, 23, 200)
        line(15, 181, 15, 219) 
        line(14, 180, 5, 180)
        line(14, 220, 5, 220)
        translate(400, 0)
        scale(-1, 1)
drawGoalPosts()
