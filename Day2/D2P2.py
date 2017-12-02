import sys, re

spreadsheet = open('D2.in','r')

# Calculate Row Difference.
def rowDifference(row):
    i = 0
    j = 0
    vals = row.split()
    
    for i in range(0, len(vals)):
        for j in range(i+1, len(vals)):
            if (int(vals[i]) % int(vals[j]) == 0):
                return int(vals[i])/int(vals[j])
            elif (int(vals[j]) % int(vals[i]) == 0):
                return int(vals[j])/int(vals[i])

    return 0

# Read the spreadsheet in line by line and calculate
# the difference between highest and lowest number
# in that line. Then add to the checksum total.
line = spreadsheet.readline()
checksum = 0
while line:
    rowDiff = rowDifference(line)
    checksum += rowDiff
    line = spreadsheet.readline()

# Print the final checksum
print(checksum)

spreadsheet.close()