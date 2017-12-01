import sys

intString = sys.argv[1]
sum = 0

for i in range(len(intString)):
    if i == (len(intString) - 1):
        if intString[i] == intString[0]:
            sum += int(intString[0])
            break
    else:
        if intString[i] == intString[i+1]:
            sum += int(intString[i+1])
    
print(sum)