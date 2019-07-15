myFoods = ["Apple", "Orange", "Mango", "Pistachio", "Bagel"]
fill(0)
textSize(20)
text("My Favourite Foods Are:", 100, 50)
fill(0, 255, 0)
for i in range(len(myFoods)):
    text(myFoods[i], 160, 100 + i * 40)