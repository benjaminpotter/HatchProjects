def setup():
	size(400, 400)
def draw():
    background(255, 255, 255)
    fill(240, 0, 0)
    noStroke()
    rect(mouseX - 90, mouseY - 30, 200, 100)
    fill(255, 255, 255)
    textSize(40)
    text("STAPLES", mouseX - 80, mouseY + 30)
