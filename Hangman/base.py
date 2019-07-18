hangman = [
    ['h','a','t','c','h'], 
    ['c','o','d','e'], 
    ['j','a','v','a','s','c','r','i','p','t'],
    ['p','y','t','h','o','n'],
    ['t','e','c','h'],
    ['c','o','m','p','u','t','e','r'], 
    ['d', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r', 's']
]
        
correct = []
incorrect = []
selection = floor(random(len(hangman)))
def start() :
  background(13, 12, 13)
  fill(244, 244, 247)
  textSize(17)
  text("Guess the word!",19,20)

def drawSpaces() :
  for i in range (0, len(hangman[selection])):
    fill(0, 0, 0)
    line( i*29 + 1, 100, i*29 + 21, 100 )

def drawText() :
  for i in range (0, len(hangman[selection])):
    for j in range (0, len(correct)) :
      if correct[j] == hangman[selection][i] :
        fill(255,255,255)
        text(hangman[selection][i], i*29 + 5, 95)

def drawIncorrect() :
  for i in range (0, len(incorrect)) :
    fill(255)
    text(incorrect[i],300,(i*23)+190)

def drawPerson() :
  stroke(245, 235, 245)
  noFill()
  line( 100, 150, 100, 350 )
  line( 100, 150, 200, 150 )
  line( 200, 150, 200, 180 )
  if len(incorrect) > 0 :
    ellipse( 200, 200, 40, 40 )
  
  if len(incorrect) > 1 :
    line( 200, 220, 200, 280 )
  
  if len(incorrect) > 2 :
    line( 200, 280, 170, 320 )
  
  if len(incorrect) > 3 :
    line( 200, 280, 230, 320 )
  
  if len(incorrect) > 4 :
    line( 200, 240, 160, 230 )
  
  if len(incorrect) > 5 :
    line( 200, 240, 240, 230 )
    fill(255, 0, 255)
    textSize(24)
    text("Game Over !", 140, 380 )
    fill(0, 255, 0)
    textSize(20)
    noLoop()
   

def checkCorrect() :
  for i in range (0, len(hangman[selection])) :
    if key == hangman[selection][i] :
      return True
    
  
  return False

def checkWin() :
  total = 0
  for i in range (0, len(hangman[selection])) :
    for j in range (0, len(correct)) :
      if correct[j] == hangman[selection][i] :
        total+=1
      
    
  
  if total == len(hangman[selection]) :
    return True
  
  else :
    return False
  

def draw() :
  start()
  drawSpaces()
  drawText()
  drawIncorrect()
  drawPerson()
  if checkWin() == True :
    fill(0,0,255)
    text("You Did It!",200,370)
  

def keyPressed(e) :
  if checkCorrect() == True :
    correct.append(key)
  
  if checkCorrect() == False :
    incorrect.append(key)
