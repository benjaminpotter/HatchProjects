center=270
speed=1.4
def drawSetup():
  translate(200,300)
  rotate(270)
  background(150, 120, 184)
  strokeWeight(1)
  fill(177, 243, 245)
  ellipse(0, 0, 20, 20)

def swingMetronome():
  if center>290 :
    speed=-speed
  elif center<250 :
    speed=-speed
  center=center+speed

def drawMetronome():
  rotate(center)
  strokeWeight(0.1)
  fill(71, 207, 222,150)
  rect(-15, 80, 30, 30)
  strokeWeight(0.1)
  fill(71, 96, 222,150)
  rect(-7.5, 80, 15, 30)
  strokeWeight(6)
  line(0,0,0,200)
  resetMatrix()

def draw() :
  drawSetup()
  swingMetronome()
  drawMetronome()
