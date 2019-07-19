def mouseDragged():
   noFill()
   ellipseMode(CORNER)
   stroke(mouseX, mouseY, mouseX - mouseY)
   arc(0, 0, mouseX, mouseY, 0, mouseY)
   ellipseMode(CENTER)
   arc(400 - mouseX, 400 - mouseY, mouseX, mouseY, 0, mouseX)
