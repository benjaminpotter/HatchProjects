# This is a comment
# They are used to help explain code
# You do not need to type these

# Variable Declaration
mode = 'none' #To know which way the scale is tipping
tipAmount = 0 #How much it is tipping
tipSpeed = 0 #How fast it tips
gameOver = False #If it has tipped too far
balance1 = 'WORK' #Text on the left
balance2 = 'FAMILY' #Text on the right

# Calling functions to set up the program
textAlign(CENTER) #Changes the alignment of text
# This is a function to draw the scale
def drawScale():
    translate(200, 200) #Set point (200,200) as (0,0)
    strokeWeight(1) #Change the thickness of the stroke
    fill(200, 167, 200) #Change the colour of the shapes
    triangle(0, 0, -100, 190, 100, 190) #Draw a triangle
    strokeWeight(10) #Change the thickness of the stroke
    fill(0) #Change the colour of the shapes
    textSize(30) #Change the text size
    rotate(tipAmount) #Rotate the entire canvas
    text(balance1, -100, -10) #Write the text on the left
    text(balance2, 100, -10) #Write the text on the right
    line(-150, 0, 150, 0) #Draw a line
    resetMatrix() #Reset all transformations
  
# This is a function that changes the amount of rotation
def moveScale(): 
    global tipAmount, tipSpeed, mode
    # If we are tipping to the left
    if mode == 'left':
        tipAmount -= 0.5 + tipSpeed #Decrease tipAmount
    # If we are tipping to the right
    if mode == 'right':
        tipAmount += 0.5 + tipSpeed #Increase tipAmount
    tipSpeed += 0.20 #Continually increase the tipSpeed
    
#This is a function to check if the game has ended
def checkGameState():
    global gameOver
    #If the tip amount has gotten too low or too high
    if tipAmount > 50 or tipAmount < -50:
        gameOver = True; #Set gameOver to true

#This is the "control center" of the program
def draw():
    global gameOver
    
    background(232, 222, 200) #Change the background colour
    drawScale() #Make everything in drawBalance happen 
    checkGameState() #Make everything in checkGameState happen
    #Test if the game is over or not
    if not gameOver: #If it isn't
        moveScale() #Make everything in moveBalance happen
    else:
        fill(0) #Change the fill colour to black
        textSize(30) #Change the text size
        text("GAME OVER", 200, 50) #Display the text

#This only happens when a key on the keyboard is pressed
def keyPressed(e):
    global mode, tipSpeed
    
    if keyCode == LEFT_ARROW: #If that key was the left arrow key
        print(key)
        mode = 'left' #Change it to left mode
        tipSpeed = 0 #Reset the tipSpeed
    if keyCode == RIGHT_ARROW: #If that key was the right arrow key
        print(key)
        mode = 'right' #Change it to right mode
        tipSpeed = 0 #Reset the tip speed