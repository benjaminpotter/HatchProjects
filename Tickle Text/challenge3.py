def setup():
    size(400, 400)
    
    global txtS
    textSize(txtS)
    textAlign(CENTER, CENTER)
    
message = "Tickle me"
x = 200
y = 200
txtS = 50

# var img = getImage("animals/rabbit");

def draw():
    global message, x, y, txtS #, img
    
    background(255)
    
    fill(200, 100, 150)
    
    # image(img, 200, yPos)
    text(message, x, y)
    
    if mouseX > x - (textWidth(message) / 2) and mouseX < x + (textWidth(message) / 2) and mouseY < y + (txtS / 2) and mouseY > y - (txtS / 2):
        x += round(random(-5, 5))
        y += round(random(-5, 5))
        
    if x > 400:
        x = 200
    elif x < 0:
        x = 200
        
    if y > 400:
        y = 200
    elif y < 0:
        y = 200
