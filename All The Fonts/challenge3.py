mono = createFont("monospace")
verdana = createFont('verdana')
georgia = createFont('georgia')
comic = createFont('comic sans ms')
arialBlack = createFont('arial black’)
courierNew = createFont('Courier New')

def drawText():
  fill(200, 0, 0)
  textFont(georgia, 30)
  text("Georgia", 200, 20)
  fill(0, 200, 0)
  textFont(mono, 30)
  text("MonoSpace", 200, 80)
  fill(0, 0, 200)
  textFont(verdana, 30)
  text("Verdana", 200, 150)
  fill(200, 200, 0)
  textFont(comic, 30)
  text("Comic Sans", 200, 230)
  fill(200, 0, 200)
  textFont(arialblack, 30)
  text("Arial black", 200, 300)
  fill(0, 200, 200)
  textFont(CourierNew, 30)
  text("Courier New", 200, 370)
drawText()