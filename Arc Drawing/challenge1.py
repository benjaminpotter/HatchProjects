var mouseDragged = function(){
    noFill();
    ellipseMode(CORNER);
    stroke(random(mouseX, mouseY), random(mouseX, mouseY), random(102,200));
    arc(0, 0, mouseX, mouseY, 0, mouseY);
};
