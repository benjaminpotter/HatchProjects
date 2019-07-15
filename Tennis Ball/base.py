def setup():
	size(400, 400)

def draw_ball() :
  background(109, 189, 199)
  noStroke()
  fill(181, 245, 52)
  ellipse(200, 200, 300, 300)

draw_ball()

def draw_stitches() :
  stroke(255, 255, 255)
  strokeWeight(10)
  noFill()
  arc(0, 200, 275, 350, 322, 399)
  arc(400, 200, 275, 350, 142, 219)

draw_stitches()
