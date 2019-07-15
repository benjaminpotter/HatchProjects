def mouse_dragged() :
    noFill()
    ellipseMode(CORNER)
    stroke(239, random(150,215), random(102,200))
    arc(0, 0, mouseX, mouseY, 0, mouseY)
