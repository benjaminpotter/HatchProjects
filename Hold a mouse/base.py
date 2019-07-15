def setup():
      size(400, 400)
def draw() :
    if mouseX < 150:
        background(255, 0, 0)
    elif mouseX < 250:
        background(0, 0, 255)
    else:
        background(0, 255, 0)
