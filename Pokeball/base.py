def setup():
    size(400, 400)
    background(255)
    drawBall()
    drawBallCenter()

def drawBall ():
  stroke(0, 0, 0)
  strokeWeight(5)
  fill(199, 12, 12)
  arc(200, 200, 250, 250, 180, 360)
  fill(255, 255, 255)
  arc(200, 200, 250, 250, 0, 180)

def drawBallCenter():
  strokeWeight(15)
  ellipse(200, 200, 75, 75)
  line(81, 200, 156, 200)
  line(245, 200, 318, 200)
  noFill()
  strokeWeight(5)
  ellipse(200, 200, 40, 40)