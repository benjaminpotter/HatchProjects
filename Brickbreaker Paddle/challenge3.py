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

def movingPaddle1() :
   fill(18, 6, 18)
   rect(Paddle1["x"], Paddle1["y"], Paddle1["width"], Paddle1["height"])
   Paddle1["y"] = mouseY - (Paddle1["height"] / 2) 

def movingPaddle2() :
   fill(18, 6, 18)
   rect(Paddle2["x"], Paddle2["y"], Paddle2["width"], Paddle2["height"])
   if keyPressed and keyCode == UP :
       Paddle2["y"] -= 5 
   if keyPressed and keyCode == DOWN :
       Paddle2["y"] += 5 
 

def draw() :
   background(232, 255, 248)
   movingPaddle1()
   movingPaddle2()
