sunset = 0
speed = 2.9
x = 100
y = 100

def draw():
   global sunset, speed, x, y
   sunset += speed
   background(0, 255, 221)
   fill(255, 221, 0)
   x += 10
   y = 300 - (((-1 / 679) * pow((x - 131), 2)) + 235)
   ellipse(x, y, 50, 50)
   fill(80, 219, 0)
   rect(0, 200, 400, 200)
   fill(0, 0, 0, sunset * 1.2)
   rect(0, 0, 400, 400)
