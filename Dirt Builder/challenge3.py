grass = getImage("minecraft/block-grass")
lava = getImage("minecraft/block-lava")
water = getImage("minecraft/block-water")
img = grass

def mouseClicked():
   imageMode(CENTER, CENTER)
       if mouseX >= 50 and mouseX <= 100 and mouseY >= 320 and mouseY <= 380 :
           img = lava
       elif mouseX >= 170 and mouseX <= 225 and mouseY >= 320 and mouseY <= 380 :
           img = grass
       elif mouseX >= 290 and mouseX <= 345 and mouseY >= 320 and mouseY <= 380 :
           img = water
       else :
           image(grass, 200, 350, 60, 60)
           image(lava, 80, 350, 60, 60)
           image(water, 320, 350, 60, 60)
   image(img, mouseX, mouseY, 50, 50)
