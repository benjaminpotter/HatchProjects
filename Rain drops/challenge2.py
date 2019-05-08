def draw ():
	draw_raindrop(56, 155, 242)
	draw_raindrop(56, 220, 56)

def draw_raindrop (r, g, b):
  raindrop_size = map(mouseX, 0, width, 2, 18)

  x = round (random(width))
  y = round (random(height))

  fill(r, g, b, 50)
  noStroke()
  ellipse(x, y, raindrop_size, raindrop_size)