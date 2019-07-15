def setup():
	size(400, 400)
def draw_background() :
  background(204, 234, 252)
  fill(255, 255, 255)
  noStroke()
  ellipse(100, 400, 300, 200)
  ellipse(300, 400, 400, 150)

draw_background()

def draw_snowman():
  stroke(100)
  ellipse(200, 300, 150, 150)
  ellipse(200, 200, 125, 125)
  ellipse(200, 125, 100, 100)
  fill(255, 131, 0)
  ellipse(186, 105, 10, 10)
  ellipse(216, 105, 10, 10)
  fill(255, 131, 0)
  triangle(200, 125, 200, 140, 230, 130)

draw_snowman()
