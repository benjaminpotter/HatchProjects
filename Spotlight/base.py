def setup():
    size(400, 400)

imageMode(CENTER)
def draw():
    spotlight = dist(mouseX, mouseY, 200, 200) + 100
    background(0, 0, 0)
    noStroke()
    fill(255, 255, 0, 50)
    tint(255 - spotlight, 255 - spotlight, 255 - spotlight)
    ellipse(mouseX, mouseY, 200, 50)
    ellipse(400 - mouseX, mouseY, 200, 50)
    image(getImage("creatures/ohnoes"), 200, 200, 100, 100)
    triangle(0, 0, mouseX - 100, mouseY, mouseX + 100, mouseY)
    triangle(400, 0, 400 - mouseX - 100, mouseY, 400 - mouseX + 100, mouseY)