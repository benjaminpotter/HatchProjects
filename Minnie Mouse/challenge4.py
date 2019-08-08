clicked = 0

def drawHead():
   fill(0, 0, 0)
   noStroke()
   ellipse(200, 200, 200, 200)
   ellipse(100, 120, 120, 120)
   ellipse(300, 120, 120, 120)

def drawSmile():
   fill(221, 194, 150)
   ellipse(180, 190, 80, 140)
   ellipse(220, 190, 80, 140)
   ellipse(200, 255, 170, 90)
   fill(0, 0, 0)
   ellipse(180, 190, 30, 70)
   ellipse(220, 190, 30, 70)
   arc(200, 260, 59, 23, 360, 543)

def drawSad():
   fill(221, 194, 150)
   ellipse(180, 190, 80, 140)
   ellipse(220, 190, 80, 140)
   ellipse(200, 255, 170, 90)
   fill(0, 0, 0)
   ellipse(180, 190, 30, 70)
   ellipse(220, 190, 30, 70)
   arc(200, 260, 59, 23, 180, 360)

def drawBow ():
   fill(255, 0, 0)
   ellipse(200, 110, 50, 30)
   ellipse(160, 110, 70, 50)
   ellipse(240, 110, 70, 50)
   ellipse(170, 80, 65, 70)
   ellipse(230, 80, 65, 70)
   fill(255, 255, 255)
   ellipse(160, 60, 20, 20)
   ellipse(230, 70, 20, 20)
   ellipse(180, 90, 20, 20)
   ellipse(145, 120, 20, 20)
   ellipse(250, 120, 20, 20)

def mouseClicked(e):
   global clicked
   if clicked == 0 :
       drawHead()
       drawSmile()
       drawBow()
       clicked = 1
  
   else :
       drawHead()
       drawSad()
       drawBow()
       clicked = 0
