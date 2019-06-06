def setup():
    size(400, 400)
    
    rectMode(CENTER)
    
    i = 400
    while i > 0:
        fill(random(255), random(255), random(255))
        rect(200, 200, i, i)
        i -= 100

#not a for loop but you cant adjust the loop control variable manually like
#js so i believe this is the best solution