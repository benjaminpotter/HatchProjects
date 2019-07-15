def draw ():
    noStroke()
    fill(255)
    
    if mouseX < 150:
        background (255, 0, 0)
        ellipse(200, 200, 50, 50)
    elif mouseX < 250:
        background(0, 0, 255)
        rect(175,175,50,50)
    else:
        background(0, 255, 0)
        ellipse(200, 200, 50, 30)