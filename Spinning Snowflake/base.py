circleArrays = [[],[],[],[],[],[],[]]
numPerLevel = 6
spinSpeed = 1
class circle :
    def __init__(self, size, color, x, y, position,rotation,speed):
        self.color = color(random(100,255),random(200,255),random(200,255))
        self.size = size
        self.x = 0
        self.y = position
        self.rotation = rotation
        self.speed = speed

def createCircleArray():
  for i in range (0, len(circleArrays)):
    for j in range (0, numPerLevel):
      circleArrays[i].append(circle((i+1)*5,i*30,(360/numPerLevel)*j,spinSpeed, rotation, speed))
    spinSpeed *= -1

createCircleArray()
def drawCircles():
  for i in range (0, len(circleArrays)):
    for j in range (0, numPerLevel):
      translate(200,200)
      rotate(circleArrays[i][j].rotation)
      circleArrays[i][j].rotation += circleArrays[i][j].speed
      circleArrays[i][j].color = color(random(100,255),random(200,255),random(200,255))
      fill(circleArrays[i][j].color)
      ellipse(0,circleArrays[i][j].y,circleArrays[i][j].size,circleArrays[i][j].size)
      resetMatrix()

def draw():
  background(0,0,0)  
  drawCircles()
