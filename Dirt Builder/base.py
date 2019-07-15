def setup():
	size(400, 400)
img = getImage("minecraft/block-grass")
imageMode(CENTER, CENTER)
def mouseClicked() :
  image(img, mouseX, mouseY, 50, 50)
