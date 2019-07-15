def setup():
      size(400, 400)
setup()
chomp_speed = 5
pac_mouth = 1
pac_mouth_close = 0

def draw():
    background(0)
    fill(255, 255, 0)
    pac_mouth_close = 360 - pac_mouth
    arc(200, 200, 80, 80, pac_mouth, pac_mouth_close)
    if pac_mouth >= 45 or pac_mouth <= 0 :
        chomp_speed *= -1

pac_mouth += chomp_speed
