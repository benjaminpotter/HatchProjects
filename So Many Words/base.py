word = "SOMANYWORDS"
mainColor = color(255,255,255)
secondaryColor = color(255,0,0)
coloredWord = 7
backgroundColor = color(0,0,0)
wordSize = 15
multipleWords = []
counter = 0
wordLength = word.length
background(backgroundColor)

def combineText():
  for i in range (0, 300):
    multipleWords = multipleWords + word
combineText()

def drawText():
  textSize(wordSize)
  start = wordLength*coloredWord-1
  for y in range (-20, 500, 50):
    for x in range (10; 400, 29):
      if counter > start and counter <= start+wordLength :
        fill(secondaryColor)
      else:
        fill(mainColor)
      text(multipleWords[counter],x,y)
      counter++
drawText()
