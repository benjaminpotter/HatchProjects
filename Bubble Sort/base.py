data = []
lineSpacing = 20
swapped = True
i = 1
strokeWeight(10)
frameRate(5)
def randomArray(n, min, max) :
  for j in range (0, n) :
    data[j] = random(min, max)

randomArray(15,0,380)
def drawData(index1, index2) :
    x = lineSpacing / 2
    for j in range (0, data.length) :
        if j == index1 or j == index2 :
            stroke(255, 0, 0)
    y = 400 - data[j]
    line(x, 400, x, y)
    stroke(0)
   
    x += lineSpacing

def swap(index1, index2) :
  tmp = data[index1]
  data[index1] = data[index2]
  data[index2] = tmp

def cycleEnd ():
  if i == data.length :
    if swapped :
      i = 1
      swapped = False
    else :
      fill(255,0,0)
      text("Data Sorted",320,200)
      noLoop()

def traverseData():
  if data[i - 1] > data[i]  :
    swap(i - 1, i)
    swapped = True
  
  drawData(i - 1, i)
  i +=1

def draw ():
  background(255)
  traverseData()
  cycleEnd()
