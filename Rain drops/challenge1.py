def draw ():
    raindrop_size = map(mouseX, 0, width, 2, 100)

    x = round (random(width))
    y = round (random(height))

    fill(56, 155, 242, 50)
    noStroke()
    ellipse(x, y, raindrop_size, raindrop_size)
    