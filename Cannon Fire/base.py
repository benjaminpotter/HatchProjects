def setup():
	size(400, 400)
def ball() :
  this.x = 200
  this.y = 200
  this.z = 1
  this.size = 50
  this.xspeed = 2
  this.yspeed = 4
  this.zspeed = 0.5

my_ball = new ball()
def draw_scene():
  background(0)
  stroke(255)
  fill(0)
  rect(40, 40, 320, 320)
  line(0, 0, 40, 40)
  line(360, 360, 400, 400)
  line(360, 40, 400, 0)
  line(0, 400, 40, 360)

def move_ball() :
  if my_ball.z > 40 or my_ball.z < 0 :
    my_ball.zspeed = -my_ball.zspeed

  if my_ball.x < 0 + my_ball.z or my_ball.x > 400 - my_ball.z :
    my_ball.xspeed = -my_ball.xspeed

  if my_ball.y < 0 + my_ball.z or my_ball.y > 400 - my_ball.z :
    my_ball.yspeed = -my_ball.yspeed

  my_ball.x += my_ball.xspeed
  my_ball.y += my_ball.yspeed
  my_ball.z += my_ball.zspeed

def draw_ball() :
  fill(129)
  ellipse(my_ball.x, 400 - my_ball.z, my_ball.size - my_ball.z, 10 - (my_ball.z / 5))
  fill(255)
  ellipse(my_ball.x, my_ball.y, my_ball.size - my_ball.z, my_ball.size - my_ball.z)

def draw = function() :
  draw_scene()
  draw_ball()
  move_ball()
