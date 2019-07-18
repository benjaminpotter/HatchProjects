# This is a comment
# They are used to help explain code
# You do not need to type these

# Replace these with words you find calm
happyWords = ["Be Calm", "Deep Breaths", "Relax"]
# The opacity of the text
fadeAmount = 0
# How fast the opacity changes
fadeSpeed = 2
# The amount of blue in the background
blueFade = 210
# How fast the blue amount changes
blueFadeSpeed = 0.25
# The index of the currect word
currentWord = 0
# Sets the text size
textSize(30)
# Center aligns the text
textAlign(CENTER)
# This function changes the current word being shown
def updateWord():
    global currentWord
    currentWord += 1  # Move the currentWord up one
    # If we're on the last word
    if currentWord == len(happyWords):
        # Reset it back to the first word
        currentWord = 0

# Changes the opacity of the word
def changeFade():
    global fadeSpeed, fadeAmount
    # If the opacity is greater then 255
    #(completely opaque)
    if fadeAmount > 255:
        # Reverse the fade
        fadeSpeed = -fadeSpeed

    # If the opacity is smaller then 0
    #(completely transparent)
    if fadeAmount < 0:
        # Reverse the speed
        fadeSpeed = -fadeSpeed
        # Go to the next word in the list
        updateWord()

# Displays the text
def drawWords():
    global fadeAmount
    # The fill sets the opacity
    fill(64, 49, 10, fadeAmount)
    # Use the currentWord as an index
    # in the happyWords array
    text(happyWords[currentWord], 200, 200)
    # Update the fade amount
    fadeAmount += fadeSpeed
    # Check if the fade needs to reverse
    changeFade()

# For extra effect, fade the background slightly
def fadeBackground():
    global blueFadeSpeed, blueFade
    # Background takes red, green, blue values
    background(153, 193, blueFade)
    # Update what is the blue value
    blueFade += blueFadeSpeed
    # Contrain it between two values
    if blueFade > 230 or blueFade < 200:
        # Reverse the speed
        blueFadeSpeed = -blueFadeSpeed

# The "control center" of the project
# This happens 30 times a second
def draw():
    # Call the function that fades the background
    fadeBackground()
    # Call the function that draws the words
    drawWords()
