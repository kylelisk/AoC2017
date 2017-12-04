import sys

passphrases = open('D4.in','r')
line = passphrases.readline()
seen = set()
validCount = 0
validPass = 1

while line:
    words = line.split()
    for word in words:
        wordSorted = ''.join(sorted(word))
        if wordSorted in seen:
            validPass = 0
            break
        else:
            seen.add(wordSorted)
    if validPass == 1:
        validCount += 1

    # Reset the crap
    seen.clear()
    validPass = 1
    line = passphrases.readline()

print(validCount)