import sys

passphrases = open('D4.in','r')
line = passphrases.readline()
seen = set()
validCount = 0
validPass = 1

while line:
    words = line.split()
    for word in words:
        if word in seen:
            validPass = 0
            break
        else:
            seen.add(word)
    if validPass == 1:
        validCount += 1

    # Reset the crap
    seen.clear()
    validPass = 1
    line = passphrases.readline()

print(validCount)