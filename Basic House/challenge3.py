gatePos = 170
ellipse(50,50,50,50)
rect(0,300,400,100)
rect(100,150,200,200)
rect(175,250,50,100)
def drawGate(gateLocation):
   rect(gateLocation,310,10,40)
   rect(gateLocation+50,310,10,40)
   rect(gateLocation,330,60,4)
drawGate(gatePos)
gatePos = 10
drawGate(gatePos)
gatePos = 330
drawGate(gatePos)
quad(180, 350, 230, 350, 270, 399, 220, 399)
