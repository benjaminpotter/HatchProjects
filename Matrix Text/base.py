def draw ():
    background(0)

    for x in range(400):
        for y in range (400):
            fill(0, 255, 0, random(0, 255))

            random_character = random(0, 256)
            random_character = int (random_character)
            random_character = chr(random_character)
            
            text(random_character, x * 15, y * 15) # different way of spacing the positions
            