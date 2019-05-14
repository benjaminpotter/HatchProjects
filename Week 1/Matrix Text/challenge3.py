def draw ():
    background(0)

    r = 255
    g = 0
    b = 0 
    
    text_size = 40
    
    ascii_max = 201
    ascii_min = 200

    for x in range(400):
        for y in range (400):
            fill(r, g, b, random(0, 255))

            random_character = random(ascii_min, ascii_max)
            random_character = int (random_character)
            random_character = chr(random_character)
            
            textSize(text_size)
            text(random_character, x * text_size, y * text_size)