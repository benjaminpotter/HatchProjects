arrayOfPhrases = ["CODE", "INCREMENT", "INDENT", "SEMICOLON", "LOOP", "DRAW", "FUNCTION"]
index = 0

textSize(60)
textAlign(CENTER, CENTER)

def keyPressed(e):
   index = keyTyped
   
def draw():
   background(255, 0, 0)
   text("KEEP\nCALM\nand", 200, 150)
   text(arrayOfPhrases[index], 200, 300)
