rocks = [] 
frameRate(20) 
noStroke() 


class Rock:
  def __init__(self, color, width, height, x):
    self.color = color(random(50, 100)) 
    self.width = random(20, 50) 
    self.height = random(20, 30) 
    self.x = x

def spawnRocks():
  x = 70 
  for i in range(0, 13):
    x += 18 
    rocks.append(Rock(color, width, height, x)) 

spawnRocks() 
def drawFire():
  fill(242, 222, 0) 
  for i in range (0, 101, 50) :
    triangle(90 + i, 300, 215 + i, 300, 152 + i, random(20, 80))

  fill(255, 125, 0) 
  for i in range (0, 101, 50) :
    triangle(110 + i, 300, 195 + i, 300, 152 + i, random(90, 150))

  fill(220, 10, 10) 
  for i in range (0, 101, 50) :
    triangle(130 + i, 300, 175 + i, 300, 152 + i, random(160, 220)) 

def drawPit():
  for i in range (0, len(rocks)):
    fill(rocks[i].color) 
    ellipse(rocks[i].x, 300, rocks[i].width, rocks[i].height) 

def draw():
  background(18) 
  drawFire() 
  drawPit()
