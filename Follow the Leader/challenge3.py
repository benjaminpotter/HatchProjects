x = 200
y = 200
x2 = 100
y2 = 100
angle = 0
speed = 10

def followMouse():
   global x, y, x2, y2, angle, speed
   if dist(mouseX, mouseY, x, y) > 10 :
       angle = atan2(mouseY - y, mouseX - x)
       x += cos(angle) * speed
       y += sin(angle) * speed

   if dist(mouseX, mouseY, x2, y2) > 10 :
       angle = atan2(mouseY - y2, mouseX - x2)
       x2 += cos(angle) * speed + 2
       y2 += sin(angle) * speed


def draw():
   global x, y, x2, y2, angle, speed
   background(0)
   followMouse()
   image(getImage("avatars/mr-pink"), x, y, 50, 50)
   image(getImage("avatars/mr-pink-green"), x2, y2, 50, 50)
