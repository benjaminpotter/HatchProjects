tileColours = [color(205, 192, 180), color(238, 228, 218), color(237, 224, 200), color(242, 177, 121), color(245, 149, 99), color(246, 124, 95), color(232, 88, 59), color(237, 207, 114), color(237, 204, 97), color(237, 200, 80), color(237, 197, 63), color(238, 195, 8)]
grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
res = false
score = 0
tick = 0
noStroke()

def getEmptyTiles():
 coords = []

 for x in range (0, 3):
  for y in range (0,4):
   if !grid[x][y] :
    coords.push({x: x, y: y})

 return coords

def canMerge():
 for x in range (0, 4) :
  for y in range (0, 4):
   if x > 0 and grid[x][y] == grid[x - 1][y] :
    return true
   elif y > 0 and grid[x][y] == grid[x][y - 1] :
    return true

 return false

def addTile():
 free = getEmptyTiles()
 pos = free[floor(random(free.length))]

 if random() < 0.75 :
  grid[pos.x][pos.y] = 1
 else :
  grid[pos.x][pos.y] = 2

 tick = 15

 if free.length == 1 and !canMerge() :
  res = 'lose’

for i in range (0, random(2,5) + 1):
 addTile()

def transpose(cc):
  tempGrid = []
  for y in range (0, 4):
    row = []
    for x in range (0, 4) :
      row.append(grid[cc ? x : 3 - x][cc ? 3 - y : y])
    tempGrid.append(row)
  return tempGrid

def moveTiles() :
    move = false
    for i in range (0, 4) :
        merged = false
        for j in range (0, 4) :
            if grid[j][i] :
                movedX = j
                for k in range (0, j):
     if !grid[k][i] :
      grid[k][i] = grid[j][i]
      grid[j][i] = 0
      movedX = k
      move = true
      break

    if merged :
     merged = false
    elif movedX and grid[movedX - 1][i] === grid[movedX][i] :
     score += pow(2, grid[movedX][i] + 1)
     grid[movedX - 1][i]++
     grid[movedX][i] = 0
     merged = true
     move = true

     if grid[movedX - 1][i] === 11:
      res = 'win'
 return move

def drawBoard():
  background(237)
  textSize(42)
  textAlign(LEFT)
  fill(0)
  text('2048', 35, 60)
  textSize(14)
  text('HOW TO PLAY: Use the arrow keys to move the tiles', 35, 375)
  fill(100)
  text('join the numbers to get the 2048 tile!', 35, 80)
  fill(187, 173, 160)
  rect(70, 90, 260, 260, 3)
  rect(200, 20, 130, 40, 3)
  fill(255)
  text('Score', 245, 33)
  textAlign(CENTER)
  textSize(20)
  text(score, 264, 53)
  textAlign(CENTER, CENTER)
  for x in range (0, 4) :
    for y in range (0, 4):
      fill(tileColours[grid[x][y]])
      rect(77 + (x * 63), 97 + (y * 63), 57, 57, 3)
      if grid[x][y] :
        if tick :
          tick--
    if grid[x][y] <= 2 :
     fill(118, 110, 100)
    else :
     fill(255)
    value = pow(2, grid[x][y])
    textSize(60 / value.toString().length)
    text(value, 105 + (x * 63), 126 + (y * 63))

def gameOver():
 fill(18, 18, 18, 70)
 rect(0, 0, 400, 400)
 textSize(30)
 fill(255)
 text('You ' + res, 200, 200)

def keyPressed():
 if res or tick :
  return
 move = false;
 def keyCode():
  if UP:
   grid = transpose()
   move = moveTiles()
   grid = transpose(true)
   break
  elif DOWN:
   grid = transpose(true)
   move = moveTiles()
   grid = transpose()
   break
  elif LEFT:
   move = moveTiles()
   break
  elif RIGHT:
   grid.reverse()
   move = moveTiles()
   grid.reverse()
   break

 if move :
  addTile()

def draw():
 drawBoard()
 if res :
   noLoop()
   gameOver()
