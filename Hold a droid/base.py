def setup():
	size(400, 400)
imageMode(CENTER)
def draw():
  background(0, 0, 0)
  image(getImage("starwars/c3po"), mouseX, mouseY, 100, 100)
