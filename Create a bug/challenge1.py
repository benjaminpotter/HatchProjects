def drawBody():
   fill(90, 175, 80)
   strokeWeight(5)
   ellipse(200, 225, 100, 200)
   strokeWeight(10)
   stroke(0)
   strokeWeight(2)
   noFill()
   bezier(27, 300, 25, 265, 35, 190, 0, 175)
   bezier(160, 300, 145, 390, 30, 400, 27, 300)
   bezier(0, 125, 65, 45, 145, 180, 175, 170)
   bezier(373, 300, 375, 265, 365, 190, 400, 175)
   bezier(240, 300, 255, 390, 370, 400, 373, 300)
   bezier(400, 125, 335, 45, 255, 180, 225, 170)

def drawHead():
   fill(0, 0, 0)
   ellipse(200, 100, 80, 80)
   fill(255, 255, 255)
   ellipse(185, 95, 20, 20)
   ellipse(215, 95, 20, 20)

def draw():
   drawBody()
   drawHead()
