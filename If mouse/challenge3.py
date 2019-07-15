def draw ():    
    if mouseX < 200 and mouseY > 200:
        background(255)
    elif mouseX > 200 and mouseY > 200:
        background(255, 0, 0)
    elif mouseX > 200 and mouseY < 200:
        background(0, 255, 0)
    else:
        background(0, 0, 255)