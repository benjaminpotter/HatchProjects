def setup():
	size(400, 400)
background(191, 223, 245)
noFill()
strokeWeight(3)
def rotate_canvas() :
    resetMatrix()
  translate(200, 200)
  rotate(45)
  translate(-200, -200)

rotate_canvas()
var draw_bat = function() {
  bezier(190, 420, 200, 250, 160, 200, 160, 0)
  bezier(210, 420, 200, 250, 240, 200, 240, 0)
  arc(200, 420, 50, 20, 0, 360)
  ellipse(200, 0, 80, 25)

draw_bat()
