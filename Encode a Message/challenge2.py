def encode(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    array = list(string)
    for i in range(len(array)):
        for a in range(len(alphabet)):
            if array[i] == alphabet[a]:
                nextLetter = (a + 2) % len(alphabet)
                array[i] = alphabet[nextLetter]
                break
    return "".join(array)
    
def decode(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    array = list(string)
    for i in range(len(array)):
        for a in range(len(alphabet)):
            if array[i] == alphabet[a]:
                realLetter = (a - 2) % len(alphabet)
                array[i] = alphabet[realLetter]
    return "".join(array)

textSize(40)
fill(255, 187, 0)
textAlign(CENTER, CENTER)
text(decode(encode("hello world")), 200, 200)
