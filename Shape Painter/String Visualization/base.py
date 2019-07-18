import re

string = "I Love Hatch!"
x = 200
y = 200
prevX = 0
prevY = 0
multiplier = 7
circleSize = 10
color1 = color(102, 67, 60)
color2 = color(255, 175, 100)
color3 = color(172, 132, 123)
colors = [color1, color2, color3]

def moveDot(i):
    if re.match(string[i], "[a-g]|[A-G]") != null:
        x += random(0, 25) * multiplier
        y -= random(0, 25) * multiplier
        circleSize += random(0, 10)
    elif re.match(string[i], "[h-n]|[H-N]") != null:
        y += random(0, 25) * multiplier
        x -= random(0, 25) * multiplier
        circleSize += random(0, 10)
    elif re.match(string[i], "[o-t]|[O-T]") != null:
        x += random(0, 25) * multiplier
        y += random(0, 25) * multiplier
        circleSize += random(0, 10)
    else:
        x -= random(0, 25) * multiplier
        y -= random(0, 25) * multiplier
        circleSize -= random(0, 10)

def drawLines():
    line(prevX, prevY, x, y)

def drawDots():
    global prevX, prevY
    global x, y
    
    for i in range(len(colors)):
        stroke(colors[round(random(0, 2))])
        moveDot(i)
        if i > 0:
            drawLines()
    noStroke()
    fill(colors[round(random(0, 2))])
    ellipse(x, y, circleSize, circleSize)
    prevX = x
    prevY = y
    x = 200
    y = 200