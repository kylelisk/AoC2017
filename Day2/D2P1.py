import sys, re

spreadsheet = open('D2.in','r')

# Calculate Row Difference.
def rowDifference(row):
    vals = row.split()

    # Set high and low vals to the first value in the list
    lowVal = int(vals[0])
    highVal = int(vals[0])
    
    for val in vals:
        if int(val) < lowVal:
            lowVal = int(val)
        elif int(val) > highVal:
            highVal = int(val)

    return (highVal - lowVal)

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