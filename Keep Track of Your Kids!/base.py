# This is a comment
# They are used to help explain code
# You do not need to type these

# Variable Declaration
x = 200 # The original x value of the child
y = 200 # The original y value of the child
angle = 0 # The original angle
speed = 4 # The original speed of the child
child = getImage("cute/CharacterBoy") # Assign child to hold an image
gameState = "Intro" # Which screen of the game
textAlign(CENTER) # Center align the text

# Create a functon that displays the intro screen
def introScreen():
    background(255, 200, 100) # Set the background color
    fill(0) # Set the color of the text
    textSize(20) # Change the text size
    text("Keep Track Of Your Kids!", 200, 200) # Display the text at 200,200
    text("Click To Start", 200, 230) # Display the text at 200,230
    if mousePressed:  # If the user clicks the mouse
        gameState = "Game"
        # We're using a gameState variable because it's an easy
        # way to keep multiple "pages".
        # Later on in the code, you'll see that different things
        # happen based on what the gameState variable is

# Create a function that performs the actions for the game
def game():
    background(143, 173, 134) # Change the background color
    
    # The dist function checks the distance between the points
    # mouseX,mouseY and x,y
    if dist(mouseX, mouseY, x, y) > 10:  # If the distance is greater then 10
        angle = atan2(mouseY - y, mouseX - x) # modify the angle
        x -= cos(angle) * speed # change the characters x position
        y -= sin(angle) * speed # change the characters y position
    image(child, x, y, 90, 90) # Display the child image

# Create a function that checks if the child has left the screen
def checkGameOver():
    # Check both the x and y points of the child
    if x > 400 or x < -90 or y > 400 or y < -90:
        # If any of them are off the screen
        gameState = "Over"
        # Change the gameState to over

# Create a function that performs the correct actions
# depending on gameState
def draw():
    # Determine which state the game is in
    if gameState == "Intro":  # If it's intro
        introScreen()
        # Call the function that displays the intro
    if gameState == "Game":  # If it's game
        game()
        # Call the function that plays the game
        checkGameOver()
        # Call the function that checks if game is over
    if gameState == "Over":  # If it's over
        background(143, 173, 134)
        # Change the background color
        textSize(15)
        # Change the text size
        # Display whatever text you would like
        text("Well... I'm Sure They'll Come Back For Dinner", 200, 200)
