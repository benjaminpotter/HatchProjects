ball = {
 “xPos” : “200”,
 “yPos” : “100”,
 “xSpeed” : “random (-5, 5)”,
 “ySpeed” : “5”
}
paddle = {
 “x”: “10”,
 “y”: “373”,
 “height”: “17”,
 “width”: “81”
}
def drawObjects():
  fill(66, 66, 66)
  ellipse(ball.xPos, ball.yPos, 6, 6)
  fill(18, 6, 18)
  rect(paddle.x, paddle.y, paddle.width, paddle.height)

def updateObjects():
  ball.xPos = ball.xPos + ball.xSpeed
  ball.yPos = ball.yPos + ball.ySpeed
  paddle.x = mouseX - paddle.width / 2

def boundaryCheck():
  if ball.xPos < 0 or ball.xPos > 400 :
    ball.xSpeed = -ball.xSpeed;
  if ball.yPos < 0 :
    ball.ySpeed = -ball.ySpeed;
  elif ball.yPos > 400 :
    ball.yPos = 410
    text("Game over", 172,200)

def paddleBounce():
  if ball.yPos >= paddle.y-5 :
    if ball.xPos >= paddle.x and ball.xPos <= paddle.x+paddle.width :
      ball.ySpeed = -ball.ySpeed

def draw():
  background(209, 255, 242)
  drawObjects()
  updateObjects()
  boundaryCheck()
  paddleBounce()
