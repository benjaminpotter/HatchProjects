def setup():
    size(400, 400)
    
img = getImage("minecraft/tnt")
imageMode(CENTER, CENTER)
background(100, 100, 100)
image(img, 200, 200, 200, 200)

def draw():
    x = random(100, 200)
    if mousePressed:
        fill(random(200, 255), random(100, 200), 0, 100)
        ellipse(random(0, 400), random(0, 400), x, x)