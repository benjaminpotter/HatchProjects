def setup():
	size(400, 400)
def draw_background() :
  background(0, 238, 255)
  fill(255, 255, 0)
  ellipse(325, 50, 50, 50)
  fill(0, 255, 0)
  rect(0, 300, 400, 100)

def draw_house():
  fill(255, 0, 0)
  rect(125, 150, 150, 150)
  fill(0, 0, 255)
  triangle(125, 150, 200, 75, 275, 150)

def draw_door() :
  fill(255, 0, 255)
  rect(175, 200, 50, 100)
  fill(0, 0, 0)
  ellipse(215, 250, 10, 10)

def draw():
  draw_background()
  draw_house()
  draw_door()
