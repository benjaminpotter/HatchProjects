setup()
chomp_speed = 5
pac_mouth = 1
pac_mouth_close = 0

def background():
   if mouseX < 150 :
        background(255, 0, 0)
    elif mouseX < 250 :
        background(0, 0, 255)
    else :
        background(0, 255, 0) 

def draw():
    background()
    fill(mouseY, mouseX, mouseY)
    pac_mouth_close = 360 - pac_mouth
    arc(200, 200, 80, 80, pac_mouth, pac_mouth_close)
    if pac_mouth >= 45 or pac_mouth <= 0 :
        chomp_speed *= -1

pac_mouth += chomp_speed
