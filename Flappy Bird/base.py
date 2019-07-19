spriteRadius = 16

gravity = 0.7
jumpVelocity = gravity * -16
velocityY = 0

spriteX = width / 2
spriteY = height / 2
score = 0

gameOver = False
menu = True

pipes = [] 
lastIndex = 2

img = loadImage("https://image.shutterstock.com/image-vector/startup-business-concept-rocket-rocketship-260nw-1315904321.jpg")

class Pipe:
    
    pipeGap = spriteRadius * 9
    pipeWidth = 40
    distBetweenPipes = 400
    pipeSpeed = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.canScore = True
        
    def update(self):
        global score, gameOver 
        
        self.x -= Pipe.pipeSpeed
        if self.x + Pipe.pipeWidth < 0:
            self.setPipePosition(self.x + Pipe.distBetweenPipes, random(80, height - 80))
        
        if self.x < spriteX and self.canScore:
            self.canScore = False
            score += 1
            
        if self.isColliding(spriteX, spriteY): 
            gameOver = True
            
        if spriteY > height - spriteRadius:
            gameOver = True
        
        Pipe.updateSprite() 
        self.drawPipe()
        
    def setPipePosition(self, x, y):
        self.x = x
        self.y = y
        self.canScore = True
    
    def isColliding(self, bx, by):
        py = self.y - Pipe.pipeGap / 2
        px = bx
        
        if dist(px, py, bx, by) <= spriteRadius and (px >= self.x and px <= self.x + Pipe.pipeWidth):
            return True
            
        py = self.y + Pipe.pipeGap / 2
        if dist(px, py, bx, by) <= spriteRadius and (px >= self.x and px <= self.x + Pipe.pipeWidth):
            return True

        if bx >= self.x and bx <= self.x + Pipe.pipeWidth:
            if by <= self.y - Pipe.pipeGap / 2 or by >= self.y + Pipe.pipeGap / 2:
                return True
 
        return False   
        
    def updateSprite():
        global velocityY, spriteY
    
        velocityY += gravity
        spriteY += velocityY
        translate(spriteX, spriteY)
        rotation = constrain(velocityY / jumpVelocity * -45, -45, 45)
        rotate(rotation)
        image(img,-spriteRadius*1.5,-spriteRadius*1.5,spriteRadius*3,spriteRadius*3)
        rotate(-rotation)
        translate(-spriteX, -spriteY)
        
    def drawPipe(self):
        fill(0, 170, 0)
        rect(self.x, 0, Pipe.pipeWidth, self.y - Pipe.pipeGap / 2)
        rect(self.x, self.y + Pipe.pipeGap, Pipe.pipeWidth, height - self.y + Pipe.pipeGap / 2)
        
def pipeUpdates():
    for pipe in pipes: 
        pipe.update()

def centerText(string, y):
    textAlign(CENTER)
    fill(0)
    text(string, width / 2, y + 2)
    fill(255)
    text(string, width / 2, y)
    
def gameUpdate():
    if not gameOver:
        pipeUpdates() 

def drawText():
    if menu:
        centerText("Flappy Bird", height / 2)
        textSize(20)
        centerText("Press space to start", height / 2 + 60)
    elif gameOver:
        centerText(f"Game Over", height / 2)
        textSize(20)
        centerText(f"Score: {score}", height / 2 + 50)
    else: 
        centerText(score, 50)
        
def setupPipes():
    for i in range(3):
        pipes.append(Pipe(700 + i * Pipe.distBetweenPipes, random(80, height - 80)))
setupPipes()

def draw():
    textSize(40)
    background(0, 200, 255)
    if not menu:
        gameUpdate()
    drawText()
    
def resetGame():
  gameOver = False
  spriteY = height / 2 - 100
  score = 0
  velocityY = 0
  lastIndex = 2
  menu = True
  
  i = 0
  for pipe in pipes:
        pipe.setPipePosition(450 + i * Pipe.distBetweenPipes, random(80, height - 80))
        i += 1

def keyPressed(e):
    global menu
    
    if keyCode == 32:
        if not gameOver:
            velocityY = jumpVelocity
        elif spriteY > height + spriteRadius:
            resetGame()
            return
        if menu:
            menu = False
