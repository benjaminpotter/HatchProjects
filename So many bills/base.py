billList = [] 
chance = 20  

class Bill:
    def __init__(self):
        self.x = random(0,380) 
        self.y = -50 
        self.speed = random(2,6) 

def setup():
    textAlign(CENTER)
    size(400,400)

def drawBill():
  for i in range(len(billList)):   
    fill(252,240,235)
    rect(billList[i].x,billList[i].y,40,50)
    fill(0)
    textSize(15)
    text("BILL\n$$$",billList[i].x+20,billList[i].y+20)

def moveBill():
    for i in range(0, len(billList)):
        billList[i].y += billList[i].speed
def start():
  trial = random(0, chance)
  roundedTrial = round(trial)
  if roundedTrial == 1:
    billList.append(Bill())
def draw():
    background(144,212,200)
    moveBill() 
    start()
    drawBill()
