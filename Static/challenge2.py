def draw():
    for x in range(0, 500):
        num = random(0, 10)
        noStroke();
        if num >= 5:
            fill(0, 0, 0);
        else:
            fill(mouseX, mouseY, 255)
        rect(random(0, 400), random(0, 400), 1, 1)



