words = ["the","quick","brown","fox","jumped","over","the","lazy","dog"]
typed = ""
theKey = ""
index = 0
right = 0
wrong = 0
time = 0
charTyped = 0
def setup():
    size(400, 400)
    start = millis()
    textAlign(CENTER)
    

def displayText():
    global index
    fill(0)
    textSize(50)
    text(words[index], 200, 150)
    text(typed,200,250)  

def checkedTyped():
    if typed != words[index]:
        wrong += 1
  
if typed == words[index]:
    right += 1
    index += 1

def end():
   total = right+wrong
   wpm = (total - wrong) / (time / 60.0)
   textSize(20)
   text("You typed " + right + "/" + total + " words correctly \n in " + time + " seconds",200,150)
   text("You're typing at "+round(wpm)+" words per minute",200,350)

def timer():
  if charTyped == 1:
  
    time = floor((millis() - start)/1000)

def draw():
  background(199, 210, 137)
  timer()
  displayText()
  if index == len(words):
    end()
    noLoop()
  

def keyPressed():
    global typed
if key == ' ':
    checkTyped = False 
    typed = ""
    
  
else:
    checkTyped = True
    theKey = str(key)
    typed = typed + theKey
  
