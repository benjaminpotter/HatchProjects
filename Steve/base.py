def setup():
	size(400, 400)
def draw_head() :
  noStroke()
  fill(227, 171, 111)
  rect(40, 40, 320, 320)
  fill(82, 41, 0)
  rect(40, 40, 320, 80)
  rect(40, 40, 40, 120)
  rect(320, 40, 40, 120)

draw_head()
def draw_face():
  rect(120, 280, 160, 80)
  fill(255, 255, 255)
  rect(80, 200, 40, 40)
  rect(280, 200, 40, 40)
  fill(0, 153, 255)
  rect(120, 200, 40, 40)
  rect(240, 200, 40, 40)
  fill(227, 171, 111)
  rect(160, 280, 80, 40)

draw_face()
