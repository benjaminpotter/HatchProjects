def setup():
    size(400, 400)
    noStroke()
    rectMode(CENTER)

def draw():
    background(51)
    fill(159, 197, 230, 80)
    ellipse(mouseX, height / 2, mouseY / 2 + 10, mouseY / 2 + 10)
    fill(255, 255, 255, 80)
    ellipse(width - mouseX, height / 2, ((height - mouseY) / 2) + 10, ((height - mouseY) / 2) + 10)
