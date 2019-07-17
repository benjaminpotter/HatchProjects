def setup():
    foreGround = color(71, 41, 41)
    backGround = color(184, 83, 83)
    global backGround, foreGround
    size(400, 400)
    translate(200, 200)
    scale(0.85, 1)
    translate(-200, -200)
    noStroke()
    fill(foreGround)
    
    background(backGround)
    
 
    background(backGround)
    mainShape()
    topShape()
    drawDetails()
    
foreGround = 0
backGround = 0

    
def mainShape():
    beginShape()
    vertex(200, 375)
    vertex(40, 200)
    vertex(20, 20)
    vertex(50, 70)
    vertex(140, 85)
    vertex(160, 140)
    vertex(200, 180)
    vertex(240, 140)
    vertex(260, 85)
    vertex(350, 70)
    vertex(380, 20)
    vertex(360, 200)
    endShape()
    
    
   

def topShape():
    beginShape()
    vertex(200, 170)
    vertex(165, 135)
    vertex(125, 20)
    vertex(165, 65)
    vertex(235, 65)
    vertex(275, 20)
    vertex(235, 135)
    endShape()

  
 
 
def drawDetails():
  for i in range (0,2):
    fill(backGround)
    triangle(190, 100, 210, 100, 200, 130)
 
    fill(foreGround)
    triangle(40, 215, 180, 370, 60, 320)
   
    fill(backGround)
    quad(85, 160, 150, 180, 170, 210, 100, 190)
   
    strokeWeight(5)
    stroke(backGround)
    line(85, 120, 165, 140)
    line(85, 100, 155, 115)
    noStroke()
   
    translate(400, 0)
    scale(-1, 1)
    
