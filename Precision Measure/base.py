buttonText = "start"
clicked = false
time=0
a=1/100
challengeTime=round(random(1,5))
textAlign(CENTER,CENTER)
def mouseClicked = function()
  if mouseX>100 and mouseX<300 and mouseY>150 and mouseY<250
    clicked=!clicked

def calculate() :
  var error = abs((challengeTime-time)/challengeTime)
  var precisionPerCent = round(100-(error*100))
  text("Your click precision is: "+precisionPerCent+"%",200, 350)

def button():
  if !clicked :
    fill(85, 196, 98)
    rect(100, 150, 200, 100, 10)
    buttonText = "start"
    if time>0 :
      calculate()
  if clicked :
    fill(247, 94, 94)
    rect(100, 150, 200, 100, 10)
    buttonText = "stop"
    time=time+a
    textSize(25)
    text(time, 200, 350)
  fill(252, 252, 252)
  textSize(55)
  text(buttonText, 200, 195)

def drawSetup() :
  background(255, 255, 255)
  noStroke()
  fill(77, 77, 77)
  textSize(40)
  text("Precision Measure", 200, 60)
  fill(120, 120, 120)
  textSize(18)
  text("Press stop after "+challengeTime+" seconds!", 200, 95)

def draw() :
  drawSetup()
  button()
