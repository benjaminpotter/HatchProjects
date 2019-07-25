drawBody():
   noStroke()
   fill(132, 82, 44)
   rect(100, 123, 200, 200)
   arc(200, 125, 200, 200, 180, 360)

var drawFace():
   fill(204, 33, 81)
   ellipse(200, 152, 75, 50)
   fill(0, 0, 0)
   ellipse(165, 90, 10, 58)
   ellipse(235, 90, 10, 58)
   fill(194, 184, 184)
   ellipse(165, 70, 6, 13)
   ellipse(235, 70, 6, 13)
   ellipse(188, 143, 33, 24)

var drawBall():
   stroke(0, 0, 0)
   strokeWeight(5)
   fill(199, 12, 12)
   arc(200, 200, 150, 150, 180, 360)
   fill(255, 255, 255)
   arc(200, 200, 150, 150, 0, 180)

var drawBallCenter():
   strokeWeight(10)
   ellipse(200, 200, 50, 50)
   line(120, 200, 170, 200)
   line(225, 200, 276, 200)
   noFill()
   strokeWeight(5)
   ellipse(200, 200, 15, 15)

var draw() :
   drawBody()
   drawFace()
   image(getImage("cute/GrassBlock"), 0, 200, 400, 177)
   resetMatrix()
   translate(-100, 90)
   drawBall()
   drawBallCenter()
   resetMatrix()
