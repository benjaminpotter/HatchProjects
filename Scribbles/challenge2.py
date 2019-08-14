def mouseDragged(e):
   height = 30
   width = 15
   for i in range (0, 5) :
       stroke(100, random(170, 200), random(200, 255))
       line(mouseX + random(int(-width), 0), mouseY + random(int(-height), int(height)), mouseX + random(0, int(width)), mouseY + (random(int(-height), int(height))))
