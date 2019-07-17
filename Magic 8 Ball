answer = floor(random(0,6))
eight = getImage("space/8")
textAlign(CENTER)
def baseImage():
  background(5, 5, 5)
  textSize(19)
  fill(242, 239, 242)
  text("Does your question need an answer?",200,25)
  text("Ask The Magic 8 Ball!",200,375)
  textSize(50)

  fill(38, 38, 38)
  ellipse(200, 200, 300, 300)
  fill(255, 255, 255)
  ellipse(200, 200, 200, 200)
  image(eight, 149, 145, 120, 120)

baseImage()
def drawTriangle():
  textSize(14)
  fill(5, 5, 5)
  ellipse(200, 200, 245, 245)
  fill(60 , 0, 255)
  triangle(200, 104,280,280,120,280)
  fill(255, 255, 255)

def revealAnswer():
  if answer == 0 :
    text("You May\nRely On It", 200, 200)
  
  elif answer == 1 :
    text("My Reply\nIs Yes", 200, 220)
  
  elif answer == 2 :
    text("My Reply\nIs No", 200, 220)
  
  elif answer == 3 :
    text("Maybe", 200, 220)
  
  elif answer == 4 :
    text("Cannot\nPredict Now", 200, 220)
  
  elif answer == 5 :
    text("Never", 200, 220)
  
  elif answer == 6 :
    text("Most Likely", 200, 220)
  

def mouseClicked() :
  drawTriangle()
  revealAnswer()
