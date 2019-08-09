arrayOfPhrases = ["CODE", "INCREMENT", "INDENT", "SEMICOLON"]
index = 0

textSize(60)
textAlign(CENTER, CENTER)

def draw():
   global index
   background(255, 0, 0)
   text("KEEP\nCALM\nand", 200, 150)
   text(arrayOfPhrases[index], 200, 300)
   frameRate(2)
   for i in range (0, 1000) :
       if i == 999 :
           index+=1
   if index == 4 :
       index = 0
