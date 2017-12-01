import sys

intString = sys.argv[1]

# Global Variables
sum = 0 # Sum variable
inputLen = len(intString) # Length of input string
steps = int(inputLen/2) # How many steps ahead to compare values

for i in range(inputLen):
    if (i + steps) > (inputLen - 1):
        # Get the index for wrapping around case
        # eg. if i is 3 and input length is 4, new index will be:
        #     3 + 2 - 4 = 1. We will compare index 3 with 1.
        idx = (i + steps) - inputLen

        # If the two indices match, add it to the sum.
        if intString[i] == intString[idx]:
            sum += int(intString[idx])
    else:
        # Simple case, if the two indices match, add them to the sum
        if intString[i] == intString[i+steps]:
            sum += int(intString[i+steps])
    
print(sum)