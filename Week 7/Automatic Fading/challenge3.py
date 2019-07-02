def setup():
    size(400, 400)

colourComponent = 255
blueComponent = 0
colourChange = 5

def colourFade():
    global colourComponent, colourChange, blueComponent
    background(colourComponent, 0, blueComponent);
    colourComponent -= colourChange
    blueComponent += colourChange

def fadeInOut():
    global colourComponent, colourChange
    if colourComponent > 254 or colourComponent < 0:
        colourChange = -colourChange


def draw():
    colourFade()
    fadeInOut()