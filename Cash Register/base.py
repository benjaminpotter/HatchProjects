def setup():
	size(400, 400)
bg_color = color(120, 120, 120)
bills_and_coins = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.5]
def draw_cash_registerfunction():
    noStroke()
    fill(50, 50, 50)
    rect(50, 50, 300, 220, 0)
    fill(225, 225, 225)
    rect(87, 130, 225, 35, 0)
    fill(225, 225, 225)
    rect(87, 210, 225, 35, 0)
    fill(225, 225, 225)
    textSize(20)
    text("Cash Register", 135, 85)
    textSize(14)
    text("Cost", 90, 120)
    text("Tendered", 90, 200)

def draw():
    background(bg_color)
    draw_cash_register()
    noLoop()
    cost = prompt("Input cost", "")
    tendered = prompt("Input tendered amount", "")
    change = Math.round((tendered - cost) / 0.05) * 0.05
    fill(0, 0, 0)
    text(cost, 95, 152)
    text(tendered, 95, 232)
    
    res = []
    for i in range(0, 10):
         count = 0;
        while change >= bills_and_coins[i]:
            count++
            change -= bills_and_coins[i]
            
        res.append(count)
        
    answer = ""
    for i in range (0, 10):
        if res[i] > 0:
            answer += res[i] + "x $" + bills_and_coins[i] + "\n"
    text(answer, 70, 325)
