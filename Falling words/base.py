data = ["hello","this","is","a","program", "developed","for",
      "Hatch", "Canada", "which", "was", "originally", "created",
      "by", "Jennifer", "Dewalt”, “and”, “translated”, “by”, “NK”]
i = 0
y = []
wordFlipSpeed = 10
wordCounter = 0
wordSpeed = 3
def displayWord():
  fill(0)
  text(data[i], 150, 50)

def nextWordTimer():
  wordCounter ++
  if wordCounter > wordFlipSpeed :
    wordCounter = 0
    y.append(50)
    i ++

def showFallingWords = function(){
  for j in range (0, y.length-1):
    fill(0,0,0,50)
    text(data[j], 150, y[j])
    y[j]*= 1 + wordSpeed / 100
    if y[j] > 350 :
      y[j] = 350

def draw() :
  background(235, 235, 235)
  displayWord()
  nextWordTimer()
  showFallingWords()
