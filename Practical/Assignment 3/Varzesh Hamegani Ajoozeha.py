def findTheBestString(input, upperBound, lowerBound, diff):
    for i in range (upperBound, lowerBound):
        if input[0:upperBound] == input[upperBound:2*upperBound]:
            output = upperBound
        upperBound = upperBound + 1
    return output

input = input()
lengthInput = len(input)
upperBound = lengthInput // 3 + 1
lowerBound = lengthInput // 2 + 1
diff = lowerBound - upperBound
firstOutput = findTheBestString(input, upperBound, lowerBound, diff)
secondOutput = lengthInput % firstOutput
for i in range(0, 8, 1):
    thirdOutput = (secondOutput + i) % firstOutput
    print(input[:firstOutput][thirdOutput], end='')