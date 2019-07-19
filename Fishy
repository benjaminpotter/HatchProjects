fish = {
    "x" : random(0,200),
    "y" : 300
}
bubble = {
    "x" : fish["x"]+70,
    "y" : fish["y"],
    "xSpeed" : 0.5,
    "ySpeed" : 1.5,
    "center" : fish["x"]+70,
    "size" : random(20,70)
}
def drawBubble():
  fill(147, 205, 234)
  ellipse(bubble["x"],bubble["y"],bubble["size"],bubble["size"])
  fill(222, 247, 243)
  ellipse(bubble["x"]-8,bubble["y"]-8,bubble["size"]-30,bubble["size"]-30)
def moveBubble():
  bubble["y"] -= bubble["ySpeed"]
  bubble["x"] -= bubble["xSpeed"]
  if(bubble["x"] < bubble["center"] - 20 or bubble["x"] > bubble["center"] + 20):
    bubble["xSpeed"] = -bubble["xSpeed"]
  
  if(bubble["y"] < -50):
    bubble["y"] = fish["y"]
    bubble["x"] = fish["x"]+70
    bubblesize = random(20,70)
    bubblecenter = fish["x"]+70

def drawFish():
  fill(219, 154, 226)
  triangle(fish["x"]-60,fish["y"],fish["x"]-150,fish["y"]-50,fish["x"]-150,fish["y"]+50)
  ellipse(fish["x"],fish["y"],190,170)
  fill(255)
  ellipse(fish["x"]+70,fish["y"],20,20)
  fill(0)
  ellipse(fish["x"]+70,fish["y"],10,10)
def moveFish():
  fish["x"] += 1.5
  if(fish["x"] > 550):
    fish["x"] = -100
def draw():
  background(39, 198, 172)
  stroke(255)
  drawBubble()
  moveBubble()
  drawFish()
  moveFish()
