numPlanets = 10
arms = 11
speed = 0.015
tick = 0
translate(200, 200)
def draw() :
  background(0, 0, 0)
  tick += speed
  for s in range (10, arms * 20, 20) : 
    pushMatrix()
    for p in range (0, numPlanets) :
      fill(255, 0, 60 * p + 20)
      ellipse(0, 0, 30 / p, 30 / p)
      translate(sin(tick * p + s) * (8 / (p * 0.1)), cos(tick * p + s) * (8 /  (p * 0.1)))
    popMatrix()
