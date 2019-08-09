sunsetX = 0
sunsetY = 0
speed = 0.5

def draw():
   global sunsetX, sunsetY, speed
   sunsetX += speed
   sunsetY = 200 + sin(sunsetX / 2) * -200
   background(0, 255, 221)
   fill(255, 221, 0)
   ellipse(sunsetX, sunsetY, 50, 50)
   fill(80, 219, 0)
   rect(0, 200, 400, 200)
   fill(0, 0, 200, sunsetY)
   rect(0, 0, 400, 200)
   if sunsetX > 400 :
       sunsetX = 0
