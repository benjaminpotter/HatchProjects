count = 10
squr1 = 3
squr2 = 2
squr3 = 1
noStroke()
frameRate(9)
square = {'x': [130, 180, 230, 230, 230, 180, 130, 130], 'y': [120, 120, 120, 170, 220, 220, 220, 170], 'r': [209, 209, 209, 209, 209, 209, 209, 209], 'g': [209, 209, 209, 209, 209, 209, 209, 209], 'b': [209, 209, 209, 209, 209, 209, 209, 209]}

def drawSquares():
    for n in range(8):
        fill(square['r'][n], square['g'][n], square['b'][n])
        rect(square['x'][n], square['y'][n], 45, 45)

def updateSquares():
    count += 1
    square['r'][count % 8] = 0
    square['g'][count % 8] = 122
    square['b'][count % 8] = 166
    square['r'][(count - 1) % 8] = 145
    square['g'][(count - 1) % 8] = 215
    square['b'][(count - 1) % 8] = 255
    square['r'][(count - 2) % 8] = 209
    square['g'][(count - 2) % 8] = 209
    square['b'][(count - 2) % 8] = 209

def draw():
    updateSquares()
    drawSquares()
