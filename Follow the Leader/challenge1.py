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
   image(getImage("avatars/mr-pink"), x, y, 50, 50)
