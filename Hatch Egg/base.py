top_pos = 190
bottom_pos = 220
def draw_lines(y):
  line(100, y, 166, y - 30)
  line(166, y - 30, 232, y)
  line(232, y, 297, y - 30)

def draw_egg():
  background(0, 118, 165)
  stroke(255)
  strokeWeight(10)
  noFill()
  arc(200, top_pos, 200, 280, 180, 345)
  drawLines(top_pos)
  drawLines(bottom_pos)
  arc(200, bottom_pos, 200, 250, 346, 540);
};
draw_egg();
