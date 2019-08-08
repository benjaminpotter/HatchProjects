numBlocks = 10
blockWidth = 400/numBlocks
firstColour = color(84, 90, 204)
secondColour = color(255, 162, 0)
thirdColour = color(0, 0, 0)
noStroke()

for i in range (0, numBlocks) :
   if i%3 == 0 :
       fill(firstColour)
   elif i%3 == 1 :
       fill(secondColour)
   else :
       fill(thirdColour)
   rect(i*blockWidth, 0, blockWidth, 400)
