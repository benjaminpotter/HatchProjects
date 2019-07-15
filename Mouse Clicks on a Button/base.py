def setup():
	size(400, 400)

def drawScene() :
  background(236, 255, 196)
  fill(0, 51, 255)
  noStroke()
  rect(160, 160, 80, 40)
  fill(255, 255, 255)
  textSize(20)
  text("Click Me", 162, 185)

drawScene()

def mouseClicked() :
 if mouseX > 160 && mouseX < 240 && mouseY > 160 && mouseY < 200 :
 	background(random(0, 255), random(0, 255), random(0, 255))
 	fill(0, 0, 255)
 	rect(160, 160, 80, 40)
 	fill(255, 255, 255)
 	text("Click Me", 162, 185)
