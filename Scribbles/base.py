def setup():
	size(400, 400)
def mouseDragged() :
  height = 10
  width = 5
  for i in range (0, 5) :
    stroke(100, random(170, 200), random(200, 255))
    line(mouseX + random(-width, 0), mouseY + random(-height, height), mouseX + random(0, width), mouseY + (random(-height, height)))
