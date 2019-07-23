def drawHandle():
   fill(175, 175, 175)
   stroke(0, 0, 0)
   rect(200, 300, 22, 75, 5)
   for i in range (0, 5):
       rect(200, 320 + 10 * i, 22, 5)
   ellipse(211, 320, 10, 10)

def drawSaber():
   fill(0, 255, 255)
   noStroke()
   rect(200, 100, 22, 210, 8)
   fill(0, 255, 255, 15)
   brightness = random(5, 10)
   for i in range (0, brightness):
       rect(190, 90, 42, 220, 10)

def draw() :
 background(0, 0, 0)
 drawHandle()
 drawSaber()
