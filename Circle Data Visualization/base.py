def setup():
	size(400, 400)

numbers = [120, 2, 33, 100, 20, 55, 34, 10, 4]
circleSize = 0
sortedNumbers = sort(numbers)
sortedNumbersReverse = reverse(sortedNumbers)
noStroke()
translate(200, 200)
scale(3, 3)

def drawCircles() :
  circleSize = sortedNumbersReverse[0]
  for in in range (1, sortedNumbersReverse.length) :
    fill(random(0, 255), random(0, 255), random(0, 255))
    ellipse(0, 0, circleSize, circleSize)
    circleSize = circleSize + (sortedNumbersReverse[i + 1] - sortedNumbersReverse[i])

drawCircles()
