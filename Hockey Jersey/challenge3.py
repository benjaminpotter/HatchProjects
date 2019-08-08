jerseyColor1 = color(255,105,180)
jerseyColor2 = color(230,230,250)
name = "Johnson"
number = 68

def drawJersey():
   strokeWeight(1)
   stroke(0, 0, 0)
   fill(jerseyColor1)
   rect(100, 50, 200, 300)
   rect(50, 125, 50, 175)
   rect(300, 125, 50, 175)
   arc(101, 130, 100, 160, 180, 270)
   arc(300, 130, 100, 160, 270, 360)
drawJersey()

def drawJerseyDetails():
   fill(jerseyColor2)
   rect(100, 250, 200, 20)
   rect(100, 281, 200, 20)
   rect(50, 150, 50, 20)
   rect(300, 150, 50, 20)
drawJerseyDetails()

def printName():
   textSize(100)
   text(number, 150, 245)
   textSize(30)
   text(name, width / 2 - len(name) * 8, 165)
printName()

def drawLogo():
   noFill()
   stroke(jerseyColor2)
   strokeWeight(18)
   arc(205, 100, 80, 50, 50, 310)
   stroke(255, 255, 255)
   strokeWeight(11)
   arc(202, 100, 75, 50, 45, 314)
   strokeWeight(7)
   line(191, 83, 191, 120)
   line(210, 83, 210, 120)
   line(191, 100, 210, 100)
   stroke(jerseyColor1)
   strokeWeight(8)
   arc(202, 100, 75, 50, 45, 314)
drawLogo()
