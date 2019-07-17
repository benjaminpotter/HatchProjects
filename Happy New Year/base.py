start = 4
time = 4
ballX = 200
ballY = 100
noStroke()
textAlign(CENTER,CENTER)
def timer() :
  time = floor(start -= 1/60) 
  fill(0)
  textSize(30)
  text(time,200,30)

def ball():
  stroke(0)
  strokeWeight(30)
  line(200,100,200,400)
  noStroke()
  fill(206)
  ellipse(ballX,ballY,200,200)
  ballY += 1.25

def happyNewYear():
  background(171, 88, 176)
  fill(255)
  textSize(30)
  fill(random(0,255),random(0,255), random(0,255))
  text("HAPPY NEW YEAR",200,200)

def draw():
  background(255)
  if time == 0 :
    happyNewYear()
  else:
    timer()
    ball()
