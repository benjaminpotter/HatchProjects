data = [ 30, 10, 45, 35, 60, 38, 75, 67 ]
pieSize = 300
gray = 0
noStroke()
background(100)
def pieChart() :
 lastAngle = 0
 for i in range (0, data.length) :
  gray = map(i, 0, data.length, 0, 255)
  fill(gray)
  arc(width / 2, height / 2, pieSize, pieSize, lastAngle, lastAngle + radians(data[i]))
  lastAngle += radians(data[i])

pieChart()
