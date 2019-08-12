def minecraftBlock():
  for i in range (0, 401, 40) :
      for j in range (0, 401, 40) :
          if j < 110 :
               fill(0, random(100, 255), 0);
          elif j > 140 and j < 200 :
               fill(random(200, 255), random(200, 255), 0);
          elif (round(random(0, 1)) == 1) and j < 270 :
               fill(random(200, 255), random(200, 255), 0);
          elif j > 200 :
               fill(random(100, 140), random(30, 70), 0);
          rect(i, j, 40, 40)
minecraftBlock()
