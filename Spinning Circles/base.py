noStroke()
fill(255, 0, 13)
numOfDots = 240
angleChange = 140.3
maxRadius = 179
def dots():
  for i in range (0, numOfDots) :
    radius = maxRadius * sqrt(i / numOfDots)
    theta = angleChange * i
    x = 207 + radius * cos(theta)
    y = 200 + radius * sin(theta)
    ellipse(x, y, 5, 5)

def draw():
  background(26, 26, 26)
  dots()
  angleChange += 0.00040
