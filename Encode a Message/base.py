def encode(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    array = list(string)
    for i in range(len(array)):
        for a in range(len(alphabet)):
            if array[i] == alphabet[a]:
                nextLetter = (a + 2) % 26
                array[i] = alphabet[nextLetter]
                break
    return "".join(array)

textSize(40)
fill(120, 60, 60)
textAlign(CENTER, CENTER)
text(encode("hello world"), 200, 200)
