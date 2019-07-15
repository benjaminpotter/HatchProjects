binArray = []
binString = ""
decimal = 0
n = 128
def generateBinNumber() :
  fill(38, 0, 38)
  text("BINARY:", 90, 170)
  for j in range (0, 8) :
    binArray.push(round(random(0, 1)))
    text(binArray[j], (j * 9) + 89, 200)

generateBinNumber()
def convertNumber() :
  for j in range (0, 8) :
    decimal = decimal + binArray[j] * n
    n = n / 2

convertNumber()

def displayConversion() :
  text(decimal, 292, 197)
  text("DECIMAL:", 270, 170)

displayConversion()
