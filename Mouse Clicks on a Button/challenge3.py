class Button:
    def __init__(self, x, y, x_size, y_size, color, text):
        self.x = x
        self.y = y
        
        self.x_size = x_size
        self.y_size = y_size
        
        self.color = color
        
        self.text = text
        
    def draw_button(self):
        rectMode(CENTER)
        textAlign(CENTER, CENTER)
        
        fill(self.color)
        rect(self.x, self.y, self.x_size, self.y_size)
        
        fill(255) 
        text(self.text, self.x, self.y)
        
    def check_click(self, x, y):
        inside_x = x > self.x - (self.x_size / 2) and x < self.x + (self.x_size / 2)
        inside_y = y > self.y - (self.y_size / 2) and x < self.y + (self.y_size / 2)
        
        if inside_x and inside_y:
            return True 
            
        return False 
        
    def on_click(self):
        background(random(255), random(255), random(255))
        
buttons = [Button(100, 100, 60, 20, color(255, 100, 200), 'Click Me'), Button(200, 100, 30, 30, color(255, 200, 0), 'Q'), Button(300, 300, 50, 70, color(90, 90, 140), 'Ctl')]

def draw_buttons():
    for button in buttons:
        button.draw_button()

def draw_scene():
    background(236, 255, 196)
    draw_buttons()
draw_scene()

def draw():
    draw_buttons()

def mouseClicked(e):
    for button in buttons:
        if button.check_click(mouseX, mouseY):
            button.on_click()
