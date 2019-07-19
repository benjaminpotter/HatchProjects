entry = "";

def displayText():
    textAlign(LEFT,TOP);   
    textSize(10);
    background(192, 240, 255);    
    fill(0);
    text(entry + "_", 10, 10, 380, 400); 

def keyPressed(e):
    global entry
    
    if keyCode == 8:
        if len(entry) > 0:
            entry = entry[slice(0, (len(entry) - 1), 1)]
    displayText()

def keyTyped(e):
    global entry
    
    if keyCode == 13:
        entry += '\n' 
    else:
        entry += str(key)
    displayText()
