noStroke()
snow = []

def snowflake() :
    this.x = mouseX + random(-70,70)
    this.y = mouseY
    this.ySpeed = random(1,2)
    this.xSpeed = random(-0.5,0.5)
    this.size = random(5,15)



def drawBackground() :
    background(129,154,253)
    ellipse(100,400,400,150)
    ellipse(300,400,400,100)


def drawCloud() :
    ellipse(mouseX,mouseY,120,120)
    ellipse(mouseX-20,mouseY,120,100)
    ellipse(mouseX+20,mouseY,120,100)
    ellipse(mouseX+30,mouseY+20,150,50)
    ellipse(mouseX-30,mouseY+20,150,50)


def drawSnow() :
    if snow.length < 200 
        snow.append(new snowflake())
    
    for i in range (0, snow.length)
        ellipse(snow[i].x,snow[i].y,snow[i].size,snow[i].size)
        snow[i].x += snow[i].xSpeed
        snow[i].y += snow[i].ySpeed
        if snow[i].y > 400
            snow[i] = new snowflake()
        
    


def draw() :
    drawBackground()
    drawCloud()
    drawSnow()
