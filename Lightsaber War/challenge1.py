def draw():
   frameRate(20)
   noStroke()
   fill(0, 0, 0, 100)
   rect(0, 0, 400, 400)
   stroke(0, 255, 0, mouseY)
   strokeWeight(20)
   line(mouseX, mouseY, pmouseX, pmouseY / 3)
   stroke(255, 0, 0, 400 - mouseY)
   line(400 - mouseX, 400 - mouseY, 400 - pmouseX, 120 - pmouseY/3)
   if dist(mouseX, mouseY, 200, 200) < 30:
       noStroke()
       fill(random(0, 255), random(0, 255), random(0, 255), 200)
       rect(0, 0, 400, 400)
