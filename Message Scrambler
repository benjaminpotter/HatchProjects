message = "hello world"

def scramble(inputString) :
  array = inputString.split("")
  for i in range (0, array.length) :
    j = Math.floor(Math.random() * (i + 1))
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

  return array.join("")

textSize(30)
fill(120, 60, 60)
text(scramble(message), 128, 211)
