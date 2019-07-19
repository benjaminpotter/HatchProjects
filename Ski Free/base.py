skier = getImage("avatars/old-spice-man-blue")
skierX = mouseX
skierY = 200
speed = 2
trailX = []
trailY = []
trees = []

class Tree():
    def __init__(self):
        self.x = random(0, 400)
        self.y = random(450, 550)

class wood:
    trees.append(Tree())
    def collision(treeX, treeY): 
        if dist(skierX, skierY, treeX, treeY) < 20:
            speed = 0



def drawTrees():
    for i in range(0, trees.length): 
        trees[i].y -= speed * 2
        fill(181, 115, 34)
        rect(trees[i].x - 5, trees[i].y, 10, 30)
        fill(66, 147, 39)
        triangle(trees[i].x, trees[i].y, trees[i].x - 20, trees[i].y + 20, trees[i].x + 20, trees[i].y + 20)
        triangle(trees[i].x, trees[i].y - 10, trees[i].x - 20, trees[i].y + 10, trees[i].x + 20, trees[i].y + 10)
        triangle(trees[i].x, trees[i].y - 20, trees[i].x - 20, trees[i].y, trees[i].x + 20, trees[i].y)
        if trees[i].y < -50:
            trees[i].y = random(450, 850)
            trees[i].x = random(0, 400)
        if random(0, 10) > 7: 
            trees.append(tree())
            collision(trees[i].x, trees[i].y)
def drawSkier():
    noStroke()
    fill(165, 100, 70)
    rect(skierX + 8, skierY - 20, 7, 60, 30)
    rect(skierX - 16, skierY - 20, 7, 60, 30)
    image(skier, skierX, skierY, 50, 50)

def drawTrail():
    stroke(205, 180)
    strokeWeight(3)
    for i in range (1, len(trailX)): 
        trailY[i] -= speed
        trailY[i - 1] -= speed
        line(trailX[i - 1] + 11, trailY[i - 1], trailX[i] + 11, trailY[i])
        line(trailX[i - 1] - 13, trailY[i - 1], trailX[i] - 13, trailY[i])
        if  trailY[i] < -10: 
            trailY.splice(i, 1)
            trailX.splice(i, 1)
  
    trailX.append(skierX)
    trailY.append(skierY)

def draw():
    background(255)
    drawTrail()
    drawSkier()
    drawTrees()
    imageMode(CENTER)
    textAlign(CENTER)
    if speed != 0: 
        skierX = mouseX
    
    else:
        fill(255, 0, 0)
        textSize(20)
        text("Ouch!", skierX, skierY - 30)
 
