gaussX = 0
randX = 0

frameRate(30)
fill(0, 15)
noStroke()
def gauss(mean, standardDev):
  var radix = random() * TWO_PI
  var root = sqrt(-2 * log(1 - random()))
  var normal = cos(radix) * root
  return mean + normal * standardDev

def updateValues () :
  randX = random(0, 400)
  gaussX = gauss(200, 50)

def drawDisplay() :
  ellipse(randX, 150, 15, 15)
  ellipse(gaussX, 250, 15, 15)

def draw() :
  updateValues()
  drawDisplay()
