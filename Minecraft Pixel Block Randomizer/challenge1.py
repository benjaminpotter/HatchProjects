def minecraftBlock():
  for i in range (0, 401, 40) :
      for j in range (0, 401, 40) :
          fill(random(0, 255), random(0, 255), random(0, 255))
          rect(i, j, 40, 40)
minecraftBlock()
