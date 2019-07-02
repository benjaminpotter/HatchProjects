def setup():
    global depth
    
    size(400, 400)
    background(18)
    strokeWeight(1.5)
    drawTree(200, 400, -90, depth)

colour = [round(random(255)), round(random(255)), round(random(255))]
depth = 9

def updateColours():
    global colour
    for i in range(2):
        colour[i] += round(random(-10, 10))

def drawTree(x1, y1, angle, depth):
    global colour
    
    if depth:
        x2 = x1 + (cos(angle * PI / 180) * depth * 7)
        y2 = y1 + (sin(angle * PI / 180) * depth * 8)

        fill(colour[0], colour[1], colour[2], 10)
        stroke(colour[0], colour[1], colour[2])
        updateColours()

        num = round(random(0, 1))
        if num == 1:
            noStroke()
            ellipse(x1, y1, x2, y2)
        else:
            line(x1, y1, x2, y2)
            
        drawTree(x2, y2, angle - 20, depth - 1)
        drawTree(x2, y2, angle + 20, depth - 1)