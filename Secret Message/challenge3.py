def setup ():
    size(400, 400)
    
    background(0)
    noStroke()

x = random(0, 400)
y = random(0, 400)

def draw ():
    global x
    global y
    
    draw_text(x, y)
    
def draw_text (x, y):
    secret_message = "Coding is fun!"
    
    fill(0)
    textSize(20)
    text(secret_message, x, y)
    
    if mousePressed:
        fill(255, 255, 255, 255)
        ellipse(mouseX, mouseY, 20, 20)