def minecraftBlock():
  for i in range (0, 401, 40) :
      for j in range (0, 401, 40) :
          if j < 140 :
               fill(0, random(100, 255), 0)
          elif j > 170 :
               fill(random(100, 140), random(30, 70), 0)
          elif round(random(0, 1)) == 1 :
               fill(random(100, 140), random(40, 60), 0)
          rect(i, j, 40, 40)
minecraftBlock()
