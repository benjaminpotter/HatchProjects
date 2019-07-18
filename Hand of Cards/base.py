cards = []
background(7, 114, 65)

class Card:

    def __init__(self):
        self.suit = ""
        self.number = ""
        self.color = ""

cards.append(Card())
cards.append(Card())              
cards.append(Card())
cards.append(Card())
cards.append(Card())

def chooseSuit(card):
    num = round(random(1, 4))

    if num == 1:
        card.suit = "hearts"
        card.color = color(255, 0, 0)
    if num == 2:
        card.suit = "diamonds"
        card.color = color(255, 0, 0)
    if num == 3:
        card.suit = "spades"
        card.color = color(0, 0, 0)
    if num == 4:
        card.suit = "clubs"
        card.color = color(0, 0, 0)

def chooseNumber(card):
    num = round(random(0, 13))
    if num == 11:
        num = "J"
    if num == 12:
        num = "Q"
    if num == 13:
        num = "K"
    if num == 0:
        num = "A"
    card.number = num

def setCards():
    for card in cards:
        chooseSuit(card)
        chooseNumber(card)
setCards()

def drawSuit(card):
    noStroke()
    if card.suit == "diamonds":
        quad(-90, -340, -70, -360, -50, -340, -70, -320)
    if card.suit == "hearts":
        ellipse(-80, -340, 22, 19)
        ellipse(-65, -340, 22, 19)
        triangle(-92, -340, -53, -340, -75, -315)
    if card.suit == "spades":
        ellipse(-80, -340, 22, 19)
        ellipse(-65, -340, 22, 19)
        triangle(-92, -340, -53, -340, -75, -365)
        rect(-75, -340, 5, 20)
    if card.suit == "clubs":
        ellipse(-80, -340, 20, 20)
        ellipse(-65, -340, 20, 20)
        ellipse(-73, -355, 20, 20)
        rect(-75, -340, 5, 20)

def drawCards():
    translate(100, 500)
    for card in cards:
        stroke(0)
        rotate(10)
        fill(255)
        rect(-100, -400, 100, 200)
        fill(card.color)
        textSize(20)
        text(card.number, -75, -370)
        drawSuit(card)
drawCards()