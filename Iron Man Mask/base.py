def drawMaskBase():
    background(212, 0, 0)
    noStroke()
    fill(247, 255, 0)
    rect(122, 83, 160, 153, 6)
    quad(103, 175, 303, 178, 272, 338, 141, 338)
drawMaskBase()

def drawDetails():
    fill(255, 255, 255)
    quad(172, 245, 189, 236, 137, 208, 141, 236)
    quad(241, 245, 268, 234, 272, 208, 217, 236)
    fill(212, 0, 0)
    rect(173, 57, 57, 85)
    stroke(212, 0, 0)
    strokeWeight(2)
    line(274, 320, 137, 320)
drawDetails()