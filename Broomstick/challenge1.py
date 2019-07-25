def drawStick() :
   background(100, 150, 255) 
   stroke(200, 120, 75) 
   strokeWeight(8) 
   line(60, 125, 160, 170) 
   line(160, 170, 190, 195) 
   line(190, 195, 260, 230) 
drawStick() 

def drawBroom():
   fill(190, 135, 75)
   stroke(190, 135, 75)
   quad(245, 230, 250, 218, 320, 230, 290, 280) 
   strokeWeight(3) 
   stroke(0) 
   line(253, 216, 245, 235) 
   line(260, 217, 251, 239) 

drawBroom() 

def drawFirebolt() :
   noFill() 
   stroke(0) 
   strokeWeight(5) 
   arc(255, 165, 50, 50, 0, 90) 
   arc(197, 245, 50, 50, 1, 90) 
   arc(245, 214, 50, 50, 200, 290) 
   arc(238, 226, 50, 50, 133, 210)
drawFirebolt()
