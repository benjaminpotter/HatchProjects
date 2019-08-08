numBlocks = 5
blockWidth = 400/numBlocks
evenColor = color(84, 90, 204)
oddColor = color(255, 162, 0)
noStroke()

for i in range (0, numBlocks) :
   if i%2 == 0 :
       fill(evenColor)
   else :
       fill(oddColor)
   rect(i*blockWidth, 0, blockWidth, 400)
