def mouseDragged():
   height = 10
   width = 5
   for i in range (0, 5) :
       stroke(200, 120, 50)
       line(mouseX + random(-int(width), 0), mouseY + random(-int(height), int(height)), mouseX + random(0, int(width)), mouseY + (random(-int(height), int(height))))
