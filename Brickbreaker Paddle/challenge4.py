p1Score = 0
p2Score = 0
Paddle1 = {
   "x": 10,
   "y": 373,
   "height": 81,
   "width": 17
}

Paddle2 = {
   "x": 373,
   "y": 373,
   "height": 81,
   "width": 17
}

Ball = {
   "x": 200,
   "y": 200,
   "radius": 10,
   "xVel": random(-6, 6),
   "yVel": random(-3, 3)
}

def movingPaddle1 () :
   fill(18, 6, 18)
   rect(Paddle1["x"], Paddle1["y"], Paddle1["width"], Paddle1["height"])
   Paddle1["y"] = mouseY - (Paddle1["height"] / 2) 
   
def movingPaddle2 () :
   fill(18, 6, 18)
   rect(Paddle2["x"], Paddle2["y"], Paddle2["width"], Paddle2["height"])
   if keyPressed and keyCode == UP :
       Paddle2["y"] -= 5 
   if keyPressed and keyCode == DOWN :
       Paddle2["y"] += 5 

def drawBall () :
   ellipse(Ball["x"], Ball["y"], Ball["radius"], Ball["radius"])
   Ball["x"] += Ball["xVel"]
   Ball["y"] -= Ball["yVel"]

def resetBall () :
   Ball["x"] = 200
   Ball["y"] = 200
   Ball["xVel"] = random(-6, 6)
   Ball["yVel"] = random(-3, 3)

def updateBall () :
   global p2Score
   if (Ball["y"] - Ball["radius"] < 0) or (Ball["y"] + Ball["radius"] > 400) :
       Ball["yVel"] = Ball["yVel"]*-1
   if Ball["x"] < 20 :
       if (Ball["y"] > Paddle1["y"]) and (Ball["y"] < (Paddle1["y"] + Paddle1["height"])) :
           Ball["xVel"] = Ball["xVel"]*-1
       else :
           resetBall()
           p2Score+=1 

   if Ball["x"] > 380 :
       global p1Score
       if (Ball["y"] > Paddle2["y"]) and (Ball["y"] < (Paddle2["y"] + Paddle2["height"])) :
           Ball["xVel"] = Ball["xVel"]*-1
       else :
           resetBall()
           p1Score+=1 


def drawScores () :
   text(p1Score, 100, 100)
   text(p2Score, 300, 100)

def draw () :
   background(232, 255, 248)
   movingPaddle1()
   movingPaddle2()
   drawBall()
   updateBall()
   drawScores()
