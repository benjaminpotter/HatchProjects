brickW = 24
brickH = 11
def drawSetup() :
    background(199, 253, 255)
    fill(252, 133, 133)

def drawBricks() :
    for i in range (0, 15) :
        for j in range (0, 10) :
            rect(10 + i * 25, 26 + 11 * j, brickW, brickH)
            
Paddle = {
  "x" : 10,
  "y": 373,
  "height": 17,
  "width": 81
}

def movingPaddle():
  rect(Paddle["x"], Paddle["y"], Paddle["width"], Paddle["height"])
  Paddle["x"] = mouseX - (Paddle["width"] / 2)

def draw():
  drawSetup()
  movingPaddle()
  drawBricks()
