def draw():
  background(0, 0, 0)
  strokeWeight(10)
  for i in range(0, width):
     var r = random(0, 255)
     var x = random (0, width)
     stroke(r, r, r, 100)
     line(i, 0, x, height)
