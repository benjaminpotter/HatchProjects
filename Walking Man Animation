frameRate(6)
action = True
frameNum = 1

hipTranslateX = 200
hipTranslateY = 200

leftLegTranslateX = 2
leftLegTranslateY = 2
leftLegRotate = 2
leftShinRotate = 2
leftFootRotate = 2

rightLegTranslateX = 0
rightLegTranslateY = 0
rightLegRotate = 0
rightShinRotate = 0
rightFootRotate = 0
def updateFrames():
  global frameNum
  if action :
    frameNum+=1
  if frameNum == 7 :
    frameNum = 1

def frame1() :
  hipTranslateX = 200
  hipTranslateY = 209
 
  leftLegTranslateX = 4
  leftLegTranslateY = 12
  leftLegRotate = -26
  leftShinRotate = -17
  leftFootRotate = 37
 
  rightLegTranslateX = -4
  rightLegTranslateY = 12
  rightLegRotate = 38
  rightShinRotate = -1
  rightFootRotate = 6

def frame2():
  hipTranslateX = 200
  hipTranslateY = 200
 
  leftLegTranslateX = 6
  leftLegTranslateY = 12
  leftLegRotate = -25
  leftShinRotate = -49
  leftFootRotate = -26
 
  rightLegTranslateX = -4
  rightLegTranslateY = 12
  rightLegRotate = 17
  rightShinRotate = -17
  rightFootRotate = 0

def frame3() :
  hipTranslateX = 200
  hipTranslateY = 189
 
  leftLegTranslateX = 0
  leftLegTranslateY = 14
  leftLegRotate = 32
  leftShinRotate = -103
  leftFootRotate = 19
 
  rightLegTranslateX = 0
  rightLegTranslateY = 12
  rightLegRotate = 0
  rightShinRotate = 0
  rightFootRotate = 0

def frame4() :
  hipTranslateX = 200
  hipTranslateY = 209
 
  leftLegTranslateX = -4
  leftLegTranslateY = 12
  leftLegRotate = 38
  leftShinRotate = -1
  leftFootRotate = 6
 
  rightLegTranslateX = 4
  rightLegTranslateY = 12
  rightLegRotate = -26
  rightShinRotate = -17
  rightFootRotate = 37

def frame5() :
  hipTranslateX = 200
  hipTranslateY = 200
 
  leftLegTranslateX = -6
  leftLegTranslateY = 12
  leftLegRotate = 17
  leftShinRotate = -17
  leftFootRotate = 0
 
  rightLegTranslateX = 4
  rightLegTranslateY = 12
  rightLegRotate = -25
  rightShinRotate = -49
  rightFootRotate = -26

def frame6() :
  hipTranslateX = 200
  hipTranslateY = 189
 
  rightLegTranslateX = 0
  rightLegTranslateY = 14
  rightLegRotate = 32
  rightShinRotate = -103
  rightFootRotate = 19
 
  leftLegTranslateX = 0
  leftLegTranslateY = 12
  leftLegRotate = 0
  leftShinRotate = 0
  leftFootRotate = 0

def drawCharacter() :
  translate(hipTranslateX, hipTranslateY)
  strokeWeight(20)
 
  #right leg
  push()
  translate(rightLegTranslateX,rightLegTranslateY)
  rotate(rightLegRotate)
  line(0, 0, 0, 60)
 
  #right shin
  translate(0,60)
  rotate(rightShinRotate)
  line(0, 0, 0, 54)
 
  #right foot
  strokeWeight(12)
  translate(0,60)
  rotate(rightFootRotate)
  triangle(-58, 20, 0, -6, 14, 20)
  pop()

  #body
  strokeWeight(4)
  rect(-27,26,57,-94)
  ellipse(9,-110,-75,79)
  line(31,-68,-82,30)
  line(-26,-68,-107,0)
  ellipse(-26,-102,5,8)
  ellipse(-4,-102,5,8)
  rect(-58,64,-111,-133)

  #left leg
  push()
  strokeWeight(20)
  translate(leftLegTranslateX,leftLegTranslateY)
  rotate(leftLegRotate)
  line(0, 0, 0, 60)

  #left shin
  translate(0,60)
  rotate(leftShinRotate)
  line(0, 0, 0, 54)

  #left foot
  strokeWeight(12)
  translate(0,60)
  rotate(leftFootRotate)
  triangle(-58, 20, 0, -6, 14, 20)
  pop()
 
  resetMatrix()

def draw():
  background(255)
  updateFrames()
  drawCharacter()

 
if frameNum == 1 :
    frame1()
if frameNum == 2:
    frame2()
if frameNum == 3:
    frame3()
if frameNum == 4:
    frame4()
if frameNum == 5:
    frame5()
if frameNum == 6:
    frame6()

stroke(0)
strokeWeight(6)
line(0, 350, 400, 350)
