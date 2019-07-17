chance = 200
gameOver = FALSE
allQuaffles = []

def quaffle(xPos,yPos) :
  this.x = xPos
  this.y = yPos
  this.size = 80

keeper = {
  “x” : 200,
  “y” : 150,
  “position”: 2
}

def drawBackground() :
  background(132, 177, 188) 
  strokeWeight(10)
  noFill()
  ellipse(100,200,100,100)
  ellipse(200,100,100,100)
  ellipse(300,200,100,100)
  line(100,250,100,400)
  line(200,150,200,400)
  line(300,250,300,400)

def drawKeeper() :
  strokeWeight(3)
  fill(181, 27, 27)
  ellipse(keeper.x,keeper.y,30,100)
  fill(237, 210, 151)
  ellipse(keeper.x,keeper.y-60,50,50)
  fill(86, 63, 45)
  ellipse(keeper.x,keeper.y+35,30,30)

def moveKeeper() :
  if keeper.position == 3
    keeper.x = 300
    keeper.y = 250
  
  if keeper.position == 1 :
    keeper.x = 100
    keeper.y = 250

  if keeper.position == 2 :
    keeper.x = 200
    keeper.y = 150

def drawQuaffle(index) :
  fill(181, 27, 27)
  ellipse(allQuaffles[index].x, allQuaffles[index].y, allQuaffles[index].size, allQuaffles[index].size)

def throwQuaffle() :
  trial = round(random(0,chance))
  if trial == 1 :
    allQuaffles.push(new quaffle(300,250))
    chance--

  if trial == 2 :
    allQuaffles.push(new quaffle(100,250))
    chance--

  if trial == 3 :
    allQuaffles.push(new quaffle(200,150))
    chance--

def checkQuaffle(i):
  if allQuaffles[i].size < 10 :
    if dist(allQuaffles[i].x, allQuaffles[i].y, keeper.x, keeper.y) > 50 :
      gameOver = TRUE

    else :
      allQuaffles[i].size = 0

def updateQuaffle() :
  for i in range (i = 0 i < allQuaffles.length i++) {
    checkQuaffle(i)
    drawQuaffle(i)
    if (allQuaffles[i].size > 1 :
      allQuaffles[i].size -= 2
      allQuaffles[i].y += sin(allQuaffles[i].size/12) * 10
    else :
      allQuaffles.splice(i,1)

def over() :
  background(0,0,0)
  fill(255,255,255)
  textSize(40)
  text("GAME OVER",80,200)

def draw() :
  drawBackground()
  drawKeeper()
  moveKeeper()
  updateQuaffle()
  throwQuaffle()
  if gameOver == TRUE :
    over()

def keyPressed() :
  if keyCode == LEFT :
    keeper.position = 1

  if keyCode == UP :
    keeper.position = 2

  if keyCode == RIGHT :
    keeper.position = 3
