def mouseDragged(e):
   height = 10
   width = 5
   for i in range (0, 5) :
       stroke(200, random(170, 200), random(200, 255))
       line(mouseX + random(int(-width), 0), mouseY + random(int(-height), int(height)), mouseX + random(0, int(width)), mouseY + (random(int(-height), int(height))))
   resetMatrix()
   fill(0, 0, 0, 10)
   rect(-10, -10, 500, 500)
