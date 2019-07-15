def setup():
	size(400, 400)
data = [8, 7.7, 6, 6.5, 5.5, 8, 9, 11, 8.5, 10]
multiplier = 35
def drawBars() :
  for i in range (0, data.length) :
    fill(255, 0, 0)
    rect(5, 400, 20, (-data[i]) * multiplier)
    translate(width / data.length, 0)

drawBars()
