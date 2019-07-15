def setup():
    size(400, 400)

colourComponent = 255
colourChange = 2

def colourFade():
    global colourComponent, colourChange
    background(colourComponent, colourComponent, colourComponent)
    colourComponent -= colourChange

def fadeInOut():
    global colourComponent, colourChange
    if colourComponent > 254 or colourComponent < 0:
        colourChange = -colourChange


def draw():
    colourFade()
    fadeInOut()