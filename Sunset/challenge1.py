sunset = 0
speed = 0.5

def draw():
   global sunset, speed
   sunset += speed
   background(0, 255, 221)
   fill(255, 221, 0)
   ellipse(300 - sunset, 20 + sunset, 50, 50)
   fill(80, 219, 0)
   rect(0, 200, 400, 200)
   fill(0, 0, 0, sunset * 1.2)
   rect(0, 0, 400, 400)
