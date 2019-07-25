Paddle = {
   "x": 10,
   "y": 373,
   "height": 81,
   "width": 17
}

def movingPaddle():
   fill(18, 6, 18)
   rect(Paddle.x, Paddle.y, Paddle.width, Paddle.height)
   Paddle.y = mouseY - (Paddle.height / 2)

def draw():
   background(232, 255, 248)
   movingPaddle()
