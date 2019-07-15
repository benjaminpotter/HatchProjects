def setup():
    size(400, 400)
    textAlign(CENTER, CENTER)
    
class Pitch:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        if x > 125 and x < 275 and y > 100 and y < 300:
            self.isStrike = True
        else:
            self.isStrike = False
    
    def draw_self(self):
        strokeWeight(20)
        pitch = ""
        if self.isStrike:
            stroke(255, 0, 0)
            pitch = "Strike"
        else:
            stroke(255)
            pitch = "Ball"
        point(self.x, self.y)
        
        text(pitch, self.x, self.y + 30)
        
last_pitch = None

def pitch_ball():
    return Pitch(mouseX, mouseY)
    
def mousePressed():
    global last_pitch
    
    last_pitch = pitch_ball()
    
def draw_scene():
    global last_pitch
    
    background(45, 120, 39)
    
    noFill()
    strokeWeight(10)
    stroke(0)
    rect(125, 100, 150, 200)
    
    textSize(20)
    text("Click anywhere to pitch the ball.", 200, 50)
    
    if last_pitch != None:
        last_pitch.draw_self()
        
def draw():
    draw_scene()
