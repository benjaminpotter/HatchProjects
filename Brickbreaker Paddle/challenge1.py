def setup():
	size(400, 400)
Paddle = :
  "x": 10,
  "y": 373,
  "height": 17,
  "width": 81

def moving_paddle() :
  fill(mouseX, mouseY, 18)
  rect(Paddle.["x"], Paddle.["y"], Paddle.["width"], Paddle.["height"])
  Paddle.["x"] = mouseX - (Paddle.["width"] / 2)

def draw():
  background(232, 255, 248)
  moving_paddle()
