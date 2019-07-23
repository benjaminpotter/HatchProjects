def draw():
  mouseDist = dist(200, 200, mouseX, mouseY);
  for i in range(1,19):
     resetMatrix();
     translate(200, 200);
     rotate(i * 20);
     fill(mouseX - mouseY, mouseY, mouseX);
     ellipse(0, mouseDist, mouseDist / 2, mouseDist / 2);
