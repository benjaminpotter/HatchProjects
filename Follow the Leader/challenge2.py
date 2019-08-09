x = 200
y = 200
angle = 0
speed = 10

def followMouse():
   global x, y, angle, speed
   if dist(mouseX, mouseY, x, y) > 10 :
       angle = atan2(mouseY - y, mouseX - x)
       x += cos(angle) * speed
       y += sin(angle) * speed

def draw():
   global x, y, angle, speed
   background(0)
   followMouse()
   ellipse(x, y, 50, 50)
   if dist(mouseX, mouseY, x, y) < 10 :
       background(0, 200, 150)
       textAlign(CENTER)
       textSize(30)
       text("Game Over!", 200, 200)
