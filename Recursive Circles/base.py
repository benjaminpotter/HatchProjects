def drawCircle(middle, radius, level):  
    noStroke()
    col = color(floor(126 * level / 4.0))
    fill(col); 
    ellipse(middle, height / 2, radius * 2, radius * 2);   
    if level > 1:
        level = level - 1
        drawCircle(middle - radius / 2, radius / 2, level)
        drawCircle(middle + radius / 2, radius / 2, level)
drawCircle(width / 2, 200, 6);  
