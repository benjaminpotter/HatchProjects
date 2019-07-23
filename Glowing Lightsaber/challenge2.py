def drawHandle():
   fill(175, 175, 175)
   stroke(0, 0, 0)
   rect(200, 160, 22, 75, 5)
   for i in range (0, 4):
       rect(200, 180 + 10 * i, 22, 5)
   ellipse(211, 180, 10, 10)

def drawSaber():
   fill(175, 175, 175)
   stroke(0, 0, 0)
   rect(200, 20, 22, 150, 8)
   rect(200, 230, 22, 150, 8)
   fill(0, 255, 255, 15)
   brightness = random(5, 10)
   for i in range (0, brightness):
       rect(190, 10, 42, 160, 10)
       rect(190, 230, 42, 160, 10)
       
def draw() :
 background(0, 0, 0)
 drawHandle()
 drawSaber()
