obsidianHardness = 50
timePerHit = 1.5
timeMultiplier = 3.33
numberOfBlocks = 1
def blockCalculator():
    numberOfBlocks = round(random(1, 10))
    var timeToBreak = obsidianHardness * timePerHit * timeMultiplier * numberOfBlocks
    text("For " + numberOfBlocks + " block(s), it would take " +
         timeToBreak + " seconds.", 80, 200)

frameRate(0.2)
def draw():
    background(0, 0, 0)
    blockCalculator()