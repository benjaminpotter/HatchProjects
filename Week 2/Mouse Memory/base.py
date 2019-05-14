def setup():
    size(400, 400)
    #noStroke()

positions = []

trail_length = 60

def save_positions():
    positions.insert(0, (mouseX, mouseY))
    if len(positions) > trail_length:
        positions.remove(positions[trail_length])

def draw_trail():
    global trail_length
    
    count = 0
    for p in reversed(positions):
        ellipse(p[0], p[1], count/2, count/2)
        count += 1
        
def draw():
    background(51)
    save_positions()
    draw_trail() 