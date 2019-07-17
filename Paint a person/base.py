head = PImage
body = PImage
page = "Head"
def setup(): 
    size(400,400)
    imageMode(CENTER)
    displayInstruction()
def displayInstruction():
 fill(0)
 if page == "Head":
  text("Draw the Head", 160, 25)
 elif page == "Body":
  text("Draw the Body", 160, 25)
 noFill()
 rect(20,35,360,345)


def mouseDragged():
  fill(0)
  if mouseX > 20 and mouseX < 380 and mouseY > 35 and mouseY < 380:
    ellipse(mouseX, mouseY, 20, 20)
    
def keyPressed():
 if key == 'c' and page == "Head": 
  head = get(21,36,359,344)
  background(255)
  page = "Body"
  displayInstruction()
 elif key == 'c' and page == "Body":
  body = get(21,36,359,344)
  background(255)
  image(head, 200, 125, 170, 170)
  image(body, 200, 290, 170, 170)
  displayInstruction()
