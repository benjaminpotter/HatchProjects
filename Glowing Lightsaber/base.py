def setup():
    size(400, 400)

def draw_handle():
    fill(175, 175, 175)
    stroke(0, 0, 0)
    rect(200, 300, 22, 75, 5)
    for i in range(5):
        rect(200, 320 + 10 * i, 22, 5)
    ellipse(211, 320, 10, 10)

def draw_saber():
    fill(0, 255, 0)
    noStroke()
    rect(200, 100, 22, 210, 8)
    fill(0, 255, 0, 15)
    brightness = int(random(5, 10))
    for i in range(brightness):
        rect(190, 90, 42, 220, 10)

def draw():
    background(0, 0, 0)
    draw_handle()
    draw_saber()