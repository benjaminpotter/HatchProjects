def setup():
    size(400, 400)
    
    global txtS
    textSize(txtS)
    
message = "Tickle me"
x = 100
y = 200
txtS = 50

# var img = getImage("animals/rabbit");

def draw():
    global message, x, y, txtS #, img
    
    background(255)
    
    fill(200, 100, 150)
    
    # image(img, 200, yPos)
    text(message, x, y)
    
    if mouseX > x and mouseX < x + textWidth(message) and mouseY < y and mouseY > y - txtS:
        x += round(random(-5, 5))
        y += round(random(-5, 5))