snowflakeList = []
maxSnowflakes = 300
index = 0

def snowflake() :
  this.xPos = random(-30,430)
  this.yPos = -20
  this.size = random(3,10)
  this.ySpeed = random(3,7)
  this.xSpeed = random(-2,2)

def moveSnowflake() :
  for i in range (0, snowflakeList.length):
    snowflakeList[i].yPos += snowflakeList[i].ySpeed
    snowflakeList[i].xPos += snowflakeList[i].xSpeed
    noStroke()
    fill(255)
    ellipse(snowflakeList[i].xPos,snowflakeList[i].yPos,snowflakeList[i].size, snowflakeList[i].size)

def resetArray() :
  if index > maxSnowflakes :
    index = 0

def drawSnowflake():
  snowflakeList[index] = new snowflake()
  index++

def draw() :
  background(84, 86, 86)
  drawSnowflake()
  moveSnowflake() 
  resetArray()
