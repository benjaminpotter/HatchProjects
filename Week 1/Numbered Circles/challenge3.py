# this program will answer challenge three although the output is not very good
#
# the idea of the challenge defeats the entire purpose of the program which was
# to draw circles with increasing size and brightness based on their number
# for the third challenge you have to arrange them in a weird unexplained way
# that now when they get bigger they start to overlap each other

def setup ():
    size(400, 400)
    
    textAlign(CENTER, CENTER)
    
    for x in range(1, 11):
        for y in range(1, 11):
            draw_circle(x * 40, y * 40, x + y)
        
        
def draw_circle (x, y, num):
    circle_size = 30
    circle_multiplier = 5
    alpha_multiplier = 40
    
    fill(random(0, 255), random(0, 255), random(0, 255), num * alpha_multiplier)
    ellipse(x, y, circle_size + (num * circle_multiplier), circle_size + (num * circle_multiplier))
    
    fill(0)
    text(num, x, y)