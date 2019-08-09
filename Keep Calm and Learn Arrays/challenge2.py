arrayOfPhrases = ["CODE", "INCREMENT", "INDENT", "SEMICOLON"]
index = 0

textSize(60)
textAlign(CENTER, CENTER)

def draw():
   background(255, 0, 0)
   text("KEEP\nCALM\nand", 200, 150)
   text(arrayOfPhrases[index], 200, 300)

def keyPressed(e):
   fill(random(0, 255), random(0, 255), random(0, 255))
   index = key
